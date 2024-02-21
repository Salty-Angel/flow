from django.db import models
from django.utils import timezone


class NodeType(models.TextChoices):
    PHASE = 'PHASE'
    TASK = 'TASK'


class Node(models.Model):
    can_be_completed_by = models.ManyToManyField('Role', blank=True)
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)
    complete_on_tasks = models.BooleanField(
        default=False,
        help_text='Complete node if all depends_on are completed.',
    )
    depends_on = models.ManyToManyField('Node', related_name='children', blank=True)
    description = models.TextField()
    follows = models.ManyToManyField('Node', related_name='parents', blank=True)
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
    requires_prior = models.BooleanField(
        default=True,
        help_text='Requires prior step to be completed to complete.',
    )
    requires_tasks = models.BooleanField(
        default=True,
        help_text='Requires all tasks to be done to complete.',
    )
    title = models.CharField(max_length=100)
    node_type = models.CharField(max_length=50, choices=NodeType.choices, default=NodeType.PHASE)

    def __str__(self):
        return f'<NODE> {self.id} {self.title}'

    def set_following(self, parent):
        self.follows(parent)
        self.save()

    def set_task(self, child):
        self.depends_on.add(child)
        self.save()

    def display(self, indent_level=0):
        print(
            '\t' * indent_level,
            f'{"✅" if self.completed else "❌"}',
            f'[{self.node_type}] <{self.pk}> {self.title} ',
        )
        for n in self.depends_on.all():
            n.display(indent_level=indent_level + 1)
        for n in Node.objects.filter(follows=self):
            n.display(indent_level=indent_level)

    def complete(self, user):
        errors = []
        if self.node_type == NodeType.PHASE:
            errors += self.validate_phase_completion()
        errors += self.validate_completion(user)

        if errors:
            for error in errors:
                print('ERROR COMPLETING:', error)
            return

        self.completed = True
        self.completed_on = timezone.now()
        self.save()

        # complete any parents
        parent = Node.objects.filter(depends_on=self).first()
        if parent and parent.complete_on_tasks:
            siblings = parent.depends_on.all()
            if all((s.completed for s in siblings)):
                parent.complete(user)

        print(f'"{self.title}" completed by {user.name} at {self.completed_on}.')

    def validate_completion(self, user):
        msgs = []
        roles = self.can_be_completed_by.all()
        if roles.exists() and not roles.filter(user=user):
            msgs.append(f'Requires user to have role of {[r.name for r in roles.all()]}.')
        return msgs

    def validate_phase_completion(self):
        msgs = []
        parents = self.follows.all()
        children = self.depends_on.all()
        if parents and self.requires_prior and not all((p.completed for p in parents)):
            msgs.append(
                f'Requires prior steps {[p for p in parents if not p.completed]} to be completed first.'
            )
        if children and self.requires_tasks and not all((c.completed for c in children)):
            msgs.append(
                f'Requires all tasks {[t for t in children if not t.completed]} to be completed first.'
            )
        return msgs

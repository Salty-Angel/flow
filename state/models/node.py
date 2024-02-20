from django.db import models
from django.utils import timezone


class NodeType(models.TextChoices):
    PHASE = 'PHASE'
    TASK = 'TASK'


class Node(models.Model):
    can_be_completed_by = models.ManyToManyField('Role')
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)
    depends_on = models.ManyToManyField('Node', related_name='children')
    description = models.TextField()
    follows = models.ManyToManyField('Node', related_name='parents')
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    node_type = models.CharField(max_length=50, choices=NodeType.choices, default=NodeType.PHASE)

    def complete(self):
        self.completed = True
        self.completed_on = timezone.now()
        self.save()

    def set_parent(self, parent):
        self.follows(parent)
        self.save()

    def set_child(self, child):
        self.depends_on.add(child)
        self.save()

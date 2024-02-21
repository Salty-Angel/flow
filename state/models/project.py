from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=120)
    head = models.ForeignKey('Node', on_delete=models.DO_NOTHING, related_name='project_head')

    def __str__(self):
        return f'<Project> {self.name}'

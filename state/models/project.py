from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'<Project> {self.name}'

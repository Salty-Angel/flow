from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'<ROLE> {self.name}'

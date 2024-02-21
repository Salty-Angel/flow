from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120)
    role = models.ForeignKey('Role', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'<User> {self.name} - {self.role}'

from __future__ import unicode_literals

from django.db import models


class PersonalComputer(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.title


class License(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    pc = models.ForeignKey(PersonalComputer)

    def __str__(self):
        return self.title

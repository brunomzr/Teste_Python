from django.db import models

import sys
sys.path.append('sys.path[0] + "/.."')

class Employee(models.Model):

    first_name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    department = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.first_name
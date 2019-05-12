from django.db import models

import sys

sys.path.append('sys.path[0] + "/.."')

class Department(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

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
        blank=False,
        unique=True
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    # department = models.CharField(
    #     max_length=255,
    #     null=False,
    #     blank=False
    # )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

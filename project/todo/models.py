# todo/models
from django.db import models


class Todo(models.Model):
    """
    Todo model class
    """
    title = models.CharField(max_length=72, null=False)
    body = models.CharField(max_length=140, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        """
        Defines how the admin views the record in the database
        :return: string
        """
        return self.title

from django.db import models
import json


# Users model
class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=15, null=False)

    def __str__(self):
        return json.dumps([dict(item) for item in User.objects.all().values(
            'username',
            'password')])


class Todo(models.Model):
    title = models.CharField(max_length=72, null=False)
    body = models.CharField(max_length=140, null=False)

    def __str__(self):
        return json.dumps([dict(item) for item in TodoList.objects.all().values(
            'item')])

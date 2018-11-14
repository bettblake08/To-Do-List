from django.db import models


# Users model
class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=15, null=False)

    def __str__(self):
        return json.dumps([dict(item) for item in User.objects.all().values(
            'username',
            'password')])


class TodoList(models.Model):
    item = models.CharField(max_length=10, null=False)

    def __str__(self):
        return json.dumps([dict(item) for item in TodoList.objects.all().values(
            'item')])

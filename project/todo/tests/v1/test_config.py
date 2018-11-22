# todo/test/v1/test_config
from django.test import TestCase

from rest_framework.test import APIClient
from ...models import Todo


class ModelTestCase(TestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        super(ModelTestCase, cls).setUpClass()
        cls.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        for todo in range(3):
            todo = Todo(title='New version', body='My name is a new version')
            todo.save()

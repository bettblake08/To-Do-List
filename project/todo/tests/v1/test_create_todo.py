from .test_config import ModelTestCase
from django.urls import reverse
from rest_framework import status
from .test_data import TODO


import json


class TestCreateTodo(ModelTestCase):
    def test_non_existing_title_field(self):
        """ Test create todo  """
        response = self.client.post(
            reverse("todo"),
            TODO,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

from django.urls import reverse
from rest_framework import status

from .test_config import ModelTestCase


class TestUpdateTodo(ModelTestCase):
    """ Test suite on updating a todo"""
    def test_update_specific_todo(self):
        response = self.client.put(
            reverse("todo_detail", kwargs={'pk': 1}),
            {
                "title": "Shift time to",
                "body": "blah, blah"
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

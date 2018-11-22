from .test_config import ModelTestCase
from rest_framework import status
from django.urls import reverse


class TestGetTodoList(ModelTestCase):
    """Test get all todos"""

    def test_get_all_todos(self):
        response = self.client.get(
            reverse("todo"),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

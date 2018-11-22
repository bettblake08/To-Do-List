from django.urls import reverse
from rest_framework import status

from .test_config import ModelTestCase


class TestDeleteTodo(ModelTestCase):
    """
    Test suite for deletion of Todo items
    """
    def test_delete_todo(self):
        """
        Test method for deletion of todo item
        """
        del_response = self.client.delete(
            reverse("todo_detail", kwargs={'pk': 3})
        )

        response = self.client.get(reverse("todo_detail", kwargs={'pk': 3}))
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

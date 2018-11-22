from django.urls import reverse
from rest_framework import status
# local imports
from .test_config import ModelTestCase


class TestGetSpecificTodo(ModelTestCase):
    """
    Test suite for testing a specific to do
    """

    def test_get_specific_todo(self):
        """
        The test itself
        :return: Assertion
        """

        response = self.client.get(reverse("todo_detail", kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

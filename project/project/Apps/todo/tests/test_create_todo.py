from .test_config import ModelTestCase
from rest_framework import reverse, status
from .test_data import TODO

import json


class TestCreateTodo(ModelTestCase):
    def test_non_existing_title_field(self):
        """ Test non existing title field """
        response = self.client.post(
            reverse("todo"), json.dumps({
                "body": TODO.body
            }), format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

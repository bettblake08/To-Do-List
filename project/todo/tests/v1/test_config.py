from django.test import TestCase

from rest_framework.test import APIClient


class ModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ModelTestCase, cls).setUpClass()
        cls.client = APIClient()


import pytest
import csv

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import UserRecord


pytestmark = pytest.mark.django_db


class TestUserRecord(APITestCase):
    """
    Text case for user record
    - bulk-create
    """

    def test_user_record_create(self):
        test_file = "files/test.csv"
        test_url = reverse("upload-list")

        with open(test_file, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            count = len([r for r in reader])
            response = self.client.post(test_url, {"file": csvfile})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserRecord.objects.count(), count)

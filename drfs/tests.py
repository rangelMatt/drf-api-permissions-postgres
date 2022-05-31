from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Drf

class DrfTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_drf = Drf.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_drf.save()

    def test_drfs_model(self):
        drf = Drf.objects.get(id=1)
        actual_owner = str(drf.owner)
        actual_name = str(drf.name)
        actual_description = str(drf.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_drf_list(self):
        url = reverse("drf_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drfs = response.data
        self.assertEqual(len(drfs), 1)
        self.assertEqual(drfs[0]["name"], "rake")

    def test_get_drf_by_id(self):
        url = reverse("drf_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf = response.data
        self.assertEqual(drf["name"], "rake")

    def test_create_drf(self):
        url = reverse("drf_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        drfs = Drf.objects.all()
        self.assertEqual(len(drfs), 2)
        self.assertEqual(Drf.objects.get(id=2).name, "spoon")

    def test_update_thing(self):
        url = reverse("drf_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf = Drf.objects.get(id=1)
        self.assertEqual(drf.name, data["name"])
        self.assertEqual(drf.owner.id, data["owner"])
        self.assertEqual(drf.description, data["description"])

    def test_delete_drf(self):
        url = reverse("drf_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        drfs = Drf.objects.all()
        self.assertEqual(len(drfs), 0)
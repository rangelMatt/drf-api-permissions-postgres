from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Sound


class SoundTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_sound = Sound.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_sound.save()

    def test_sounds_model(self):
        sound = Sound.objects.get(id=1)
        actual_owner = str(sound.owner)
        actual_name = str(sound.name)
        actual_description = str(sound.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_sound_list(self):
        url = reverse("sound_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sounds = response.data
        self.assertEqual(len(sounds), 1)
        self.assertEqual(sounds[0]["name"], "rake")

    def test_get_sound_by_id(self):
        url = reverse("sound_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sound = response.data
        self.assertEqual(sound["name"], "rake")

    def test_create_sound(self):
        url = reverse("sound_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        sounds = Sound.objects.all()
        self.assertEqual(len(sounds), 2)
        self.assertEqual(Sound.objects.get(id=2).name, "spoon")

    def test_update_sound(self):
        url = reverse("sound_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sound = Sound.objects.get(id=1)
        self.assertEqual(sound.name, data["name"])
        self.assertEqual(sound.owner.id, data["owner"])
        self.assertEqual(sound.description, data["description"])

    def test_delete_sound(self):
        url = reverse("sound_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        sounds = Sound.objects.all()
        self.assertEqual(len(sounds), 0)
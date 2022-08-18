from django.test import TestCase, Client
from django.urls import reverse
import json

from rest_framework import status

from puppies.models import Puppy
from puppies.serializers import PuppySerializer

client = Client()


class GetAllPuppiesTest(TestCase):
    """Test module for GET all puppies API"""

    def setUp(self):
        Puppy.objects.create(
            name="Casper", age=3, breed="Bull dog", color="Black"
        )
        Puppy.objects.create(
            name="Muffin", age=1, breed="Chihuahua", color="White"
        )

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_puppies'))
        # get data
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GetSinglePuppyTest(TestCase):
#     def setUp(self):
#         self.casper = Puppy.objects.create(
#             name="Casper", age=3, breed="Bull dog", color="Black"
#         )
#         self.muffin = Puppy.objects.create(
#             name="Muffin", age=1, breed="Chihuahua", color="White"
#         )
#
#     def test_get_valid_single_puppy(self):
#         response = client.get(reverse('get_delete_update_puppy'), kwargs={'pk': self.casper.pk})
#         puppy = Puppy.objects.get(pk=self.casper.pk)
#         serializer = PuppySerializer(puppy)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_invalid_single_puppy(self):
    #     response = client.get(reverse('get_delete_update_puppy'), kwargs={'pk': 30})
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

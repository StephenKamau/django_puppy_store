from django.test import TestCase
from ..models import Puppy


class PuppyTest(TestCase):
    """Test module for Puppy model"""

    def setUp(self):
        Puppy.objects.create(
            name="Casper", age=3, breed="Bull dog", color="Black"
        )
        Puppy.objects.create(
            name="Muffin", age=1, breed="Chihuahua", color="White"
        )

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name="Casper")
        puppy_muffin = Puppy.objects.get(name="Muffin")
        self.assertEqual(puppy_casper.get_breed(), "Casper belongs to Bull dog breed.")
        self.assertEqual(puppy_muffin.get_breed(), "Muffin belongs to Chihuahua breed.")

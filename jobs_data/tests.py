from turtle import position
from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Job


class JobTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='test_user', password='pass')
        test_user.save()

        test_thing = Job.objects.create(owner=test_user, position="carpenter", location="remote",
                                        description="full time", status="hired", employer="Acme", notes="physical work")
        test_thing.save()

    def test_things_model(self):
        thing = Job.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_position = str(thing.position)
        actual_location = str(thing.location)
        actual_description = str(thing.description)
        actual_status = str(thing.status)
        actual_employer = str(thing.employer)
        actual_notes = str(thing.notes)
        self.assertEqual(actual_owner, "test_user")
        self.assertEqual(actual_position, "carpenter")
        self.assertEqual(actual_location, "remote")
        self.assertEqual(actual_description, "full time")
        self.assertEqual(actual_status, "hired")
        self.assertEqual(actual_employer, "Acme")
        self.assertEqual(actual_notes, "physical work")

from django.test import TestCase

from .models import User


class UserTestCase(TestCase):
    def test_create_user_and_business(self):
        user = User.objects.create(name="my name", country="us")
        self.assertTrue(user.business.exists())

    def test_edit_an_user(self):
        user = User.objects.create(name="my name", country="us")
        business = user.business.first()
        self.assertTrue(user.business.exists())

        user.name = "My other name"
        user.save()
        self.assertEqual(user.name, "My other name")
        self.assertEqual(user.business.first(), business)

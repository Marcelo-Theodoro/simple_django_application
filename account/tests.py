from django.test import TestCase

from .models import User, Business


class UserTestCase(TestCase):
    def test_create_user_and_business(self):
        user = User.objects.create(name="my name", country="us")
        self.assertTrue(Business.objects.filter(user_id=user.id).exists())

    def test_edit_an_user(self):
        user = User.objects.create(name="my name", country="us")
        business = Business.objects.filter(user_id=user.id)
        self.assertIsNone(business)

        user.name = "My other name"
        user.save()
        self.assertEqual(user.name, "My other name")
        self.assertEqual(user.id, business.user_id)


class BusinessTestCase(TestCase):
    def test_business_is_active_by_default(self):
        user = User.objects.create(name="my name", country="us")
        business = Business.objects.get(user_id=user.id)
        self.assertTrue(business.is_active)

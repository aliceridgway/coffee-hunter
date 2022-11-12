from django.test import TestCase

from accounts.models import CustomUser, Profile

from django.contrib.auth import get_user_model


class TestCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = CustomUser.objects.create_user(
            username="a", email="a@a.com", password="abc"
        )

        cls.superuser = CustomUser.objects.create_superuser(
            username="b", email="b@b.com", password="abcd1234"
        )

    def test_is_user_model(self):
        user_model = get_user_model()
        self.assertEqual(user_model, CustomUser)

    def test_create_user(self):
        self.assertEqual(self.user.username, "a")
        self.assertEqual(self.user.email, "a@a.com")

        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)

    def test_create_superuser(self):
        self.assertEqual(self.superuser.username, "b")
        self.assertEqual(self.superuser.email, "b@b.com")

        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_staff)

    def test_profile_automatically_created(self):

        self.assertTrue(Profile.objects.filter(user=self.user).exists())

        self.assertTrue(Profile.objects.filter(user=self.superuser).exists())

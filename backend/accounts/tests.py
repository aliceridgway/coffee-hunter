from django.test import Client, TestCase
from django.urls import reverse

from .models import CustomUser


class TestUserCreate(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.url = reverse("customuser-list")

    def test_can_create_user(self):

        request_content = {
            "username": "alice",
            "email": "alice@fakemail.com",
            "password": "badpassword",
        }

        response = self.client.post(self.url, data=request_content)

        self.assertEqual(response.status_code, 201)


class TestListCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.url = reverse("customuser-list")

    def test_unauthenticated_user_denied(self):
        """Test an unauthenticated user cannot view the list."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)

    def test_non_staff_user_denied(self):

        user = CustomUser.objects.create_user(
            username="regular_user", email="r@fakeemail.com", password="somepassword"
        )

        self.client.force_login(user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)

    def test_staff_user_can_view_list(self):

        user = CustomUser.objects.create_superuser(
            username="staffuser", email="s@fakemail.com", password="djfakjfdklajfkldj"
        )

        self.client.force_login(user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)


class TestCustomUserDetail(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = CustomUser.objects.create_user(
            username="a", email="a@a.com", password="abc"
        )
        cls.url = reverse("customuser-detail", args=[cls.user.pk])
        cls.client = Client()

    def test_unauthenticated_user_gets_403(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)

    def test_owner_can_view_their_account(self):

        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.client.logout()

    def test_staff_user_can_see_user_detail(self):

        superuser = CustomUser.objects.create_superuser(
            username="b", email="b@b.com", password="abc"
        )

        self.client.force_login(superuser)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.client.logout()

    def test_user_cannot_view_another_users_account(self):

        hacker = CustomUser.objects.create_user(
            username="hacker", email="hacker@mchackerson.com", password="abc123"
        )

        self.client.force_login(hacker)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)


class DeleteCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.user = CustomUser.objects.create_user(
            username="a", email="a@a.com", password="abc"
        )
        cls.client = Client()
        cls.url = reverse("customuser-detail", args=[cls.user.pk])

    def test_unauthenticated_user_cannot_delete_users(self):

        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 403)

    def test_account_owner_cannot_delete_own_account(self):

        self.client.force_login(self.user)

        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 403)

        self.client.logout()

    def test_staff_user_can_delete_account(self):
        user_id = self.user.pk

        superuser = CustomUser.objects.create_superuser(
            username="b", email="b@a.com", password="abc"
        )
        self.assertTrue(superuser.is_staff)

        self.client.force_login(superuser)

        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 204)

        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(id=user_id)


class TestUpdateCustomUser(TestCase):

    NEW_EMAIL = "alice@a.com"

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = CustomUser.objects.create_user(
            email="a@a.com", username="a", password="abc"
        )
        cls.superuser = CustomUser.objects.create_superuser(
            email="staff@a.com", username="b", password="abc"
        )
        cls.url = reverse("customuser-detail", args=[cls.user.pk])
        cls.client = Client()

    def test_unauthenticated_user_cannot_update_user(self):

        response = self.client.patch(self.url, {"email": self.NEW_EMAIL})

        self.assertEqual(response.status_code, 403)

    def test_user_can_update_own_account(self):

        self.client.force_login(self.user)
        response = self.client.patch(
            self.url, {"email": self.NEW_EMAIL}, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_staff_user_can_update_account(self):

        self.client.force_login(self.superuser)

        response = self.client.patch(
            self.url, {"email": self.NEW_EMAIL}, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_user_cannot_update_account_of_other_user(self):

        other_user = CustomUser.objects.create_user(
            username="hacker", email="hacker@mchackerson.com", password="jdfkajklm"
        )

        self.client.force_login(other_user)

        response = self.client.patch(
            self.url, {"email": self.NEW_EMAIL}, content_type="application/json"
        )

        self.assertEqual(response.status_code, 403)

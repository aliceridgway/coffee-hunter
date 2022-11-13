from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from cafes.models import Tag

USER_MODEL = get_user_model()


class TestTagViewset(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.list_url = reverse("tag-list")
        cls.client = Client()

        cls.user = USER_MODEL.objects.create_user(
            username="user", email="a@a.com", password="abcde"
        )

        cls.superuser = USER_MODEL.objects.create_superuser(
            username="superuser", email="b@a.com", password="abcde"
        )

        cls.tag = Tag.objects.create(name="Sandwiches")

        cls.detail_url = reverse("tag-detail", args=[cls.tag.id])

    def test_unauthenticated_user_can_view_tag_list(self):

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_create_tags(self):

        response = self.client.post(self.list_url, {"name": "Test Tag"})

        self.assertEqual(response.status_code, 403)

    def test_regular_user_cannot_create_tags(self):

        self.client.force_login(self.user)

        response = self.client.post(self.list_url, {"name": "Coffee"})

        self.assertEqual(response.status_code, 403)

        self.client.logout()

    def test_staff_user_can_create_tags(self):

        self.client.force_login(self.superuser)

        response = self.client.post(self.list_url, {"name": "Coffee"})

        self.assertEqual(response.status_code, 201)

        self.client.logout()

    def test_unauthenticated_user_can_retrieve_tags(self):

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_update_tags(self):

        update = {"name": "Paninis"}

        put_response = self.client.put(
            self.detail_url, update, content_type="application/json"
        )
        patch_response = self.client.patch(
            self.detail_url, update, content_type="application/json"
        )

        self.assertEqual(put_response.status_code, 403)
        self.assertEqual(patch_response.status_code, 403)

    def test_regular_user_cannot_update_tags(self):

        update = {"name": "Paninis"}

        self.client.force_login(self.user)

        put_response = self.client.put(
            self.detail_url, update, content_type="application/json"
        )
        patch_response = self.client.patch(
            self.detail_url, update, content_type="application/json"
        )

        self.assertEqual(put_response.status_code, 403)
        self.assertEqual(patch_response.status_code, 403)

        self.client.logout()

    def test_staff_user_can_update_tags(self):

        update = {"name": "Paninis"}

        self.client.force_login(self.superuser)

        put_response = self.client.put(
            self.detail_url, update, content_type="application/json"
        )
        patch_response = self.client.patch(
            self.detail_url, update, content_type="application/json"
        )

        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(patch_response.status_code, 200)

        self.client.logout()

    def test_unauthenticated_user_cannot_delete_tags(self):

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 403)

    def test_regualar_user_cannot_delete_tags(self):

        self.client.force_login(self.user)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 403)

        self.client.logout()

    def test_staff_user_can_delete_tags(self):
        self.client.force_login(self.superuser)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)

        self.client.logout()

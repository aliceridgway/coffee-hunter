from django.test import TestCase
from django.test import Client

from django.urls import reverse

from django.contrib.auth import get_user_model

from cafes.models import Cafe, Review

# Create your tests here.

USER_MODEL = get_user_model()


class TestReviewViewset(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.list_url = reverse("review-list")

        cls.owner = USER_MODEL.objects.create_user(
            username="owner", password="abc", email="a@a.com"
        )
        cls.reviewer = USER_MODEL.objects.create_user(
            username="reviewer", email="o@cafe.com", password="abcde"
        )
        cls.superuser = USER_MODEL.objects.create_superuser(
            username="b", email="b@b.com", password="bcde"
        )

        cls.cafe = Cafe.objects.create(name="Test Cafe", owner=cls.owner)

        cls.review_data = {"title": "Great Cafe", "rating": 5, "cafe": cls.cafe.id}

    def test_anyone_can_see_review_list(self):

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)

    def test_user_can_leave_review(self):

        self.client.force_login(self.reviewer)

        response = self.client.post(self.list_url, self.review_data)

        self.assertEqual(response.status_code, 201)

        self.client.logout()

    def test_unauthenticated_user_cannot_leave_review(self):

        response = self.client.post(self.list_url, self.review_data)

        self.assertEqual(response.status_code, 403)

    def test_owner_cannot_review_own_cafe(self):

        self.client.force_login(self.owner)

        response = self.client.post(self.list_url, self.review_data)

        self.assertEqual(response.status_code, 400)

        self.client.logout()


class TestReviewDetail(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()

        cls.owner = USER_MODEL.objects.create_user(
            username="owner", password="abc", email="a@a.com"
        )
        cls.reviewer = USER_MODEL.objects.create_user(
            username="reviewer", email="o@cafe.com", password="abcde"
        )
        cls.other_user = USER_MODEL.objects.create_user(
            username="otheruser", email="an@other.com", password="abcde"
        )
        cls.superuser = USER_MODEL.objects.create_superuser(
            username="b", email="b@b.com", password="bcde"
        )

        cls.cafe = Cafe.objects.create(name="Test Cafe", owner=cls.owner)

        cls.review_data = {"title": "Great Cafe", "rating": 5, "cafe": cls.cafe}

    def setUp(self):
        self.review = Review.objects.create(author=self.reviewer, **self.review_data)
        self.review_detail_url = reverse("review-detail", args=[self.review.id])

    def test_reviewer_can_delete_review(self):

        self.client.force_login(self.reviewer)

        response = self.client.delete(self.review_detail_url)

        self.assertEqual(response.status_code, 204)

        self.client.logout()

    def test_staff_user_can_delete_review(self):

        self.client.force_login(self.superuser)

        response = self.client.delete(self.review_detail_url)

        self.assertEqual(response.status_code, 204)

        self.client.logout()

    def test_another_user_cannot_delete_review(self):

        self.client.force_login(self.other_user)

        response = self.client.delete(self.review_detail_url)

        self.assertEqual(response.status_code, 403)

        self.client.logout()

    def test_reviewer_cannot_update_review(self):

        self.client.force_login(self.reviewer)

        new_data = {
            "cafe": self.cafe.id,
            "title": "Changed My Mind, I Hate It.",
            "rating": 1,
        }

        put_response = self.client.put(
            self.review_detail_url, new_data, content_type="application/json"
        )

        self.assertEqual(put_response.status_code, 405)  # 405 = METHOD NOT ALLOWED

        patch_response = self.client.patch(
            self.review_detail_url, {"rating": 1}, content_type="application/json"
        )

        self.assertEqual(patch_response.status_code, 405)

    def test_anyone_can_read_review(self):

        response = self.client.get(self.review_detail_url)

        self.assertEqual(response.status_code, 200)

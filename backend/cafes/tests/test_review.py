from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from cafes.models import Cafe, Review

USER_MODEL = get_user_model()


class TestReview(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.reviewer = USER_MODEL.objects.create_user(
            username="reviewer", email="a@a.com", password="abc123"
        )
        cls.owner = USER_MODEL.objects.create_user(
            username="owner", email="b@a.com", password="abc234"
        )
        cls.cafe = Cafe.objects.create(owner=cls.owner, name="My Cafe")

    def test_rating_cannot_be_less_than_one(self):
        review = Review(cafe=self.cafe, author=self.reviewer, rating=0)

        with self.assertRaises(ValidationError):
            review.full_clean()

    def test_rating_cannot_be_more_than_five(self):
        review = Review(cafe=self.cafe, author=self.reviewer, rating=6)

        with self.assertRaises(ValidationError):
            review.full_clean()

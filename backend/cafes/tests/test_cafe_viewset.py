from django.test import TestCase

from django.urls import reverse

from django.contrib.auth import get_user_model

from cafes.models import Cafe

USER_MODEL = get_user_model()


class TestCafeViewset(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.owner = USER_MODEL.objects.create(
            username="owner", email="a@a.com", password="abcde"
        )

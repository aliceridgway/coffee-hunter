from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

USER = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cafe(models.Model):
    owner = models.ForeignKey(to=USER, related_name="cafes", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(to=Tag, related_name="cafes", blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(
        to=USER, related_name="reviews", on_delete=models.CASCADE
    )
    cafe = models.ForeignKey(to=Cafe, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cafe.id}: {self.title}"

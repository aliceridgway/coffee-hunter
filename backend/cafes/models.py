from django.db import models

from django.contrib.auth import get_user_model

USER = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cafe(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(to=Tag, related_name="cafes", blank=True)
    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(to=USER, related_name="reviews", on_delete=models.CASCADE)
    cafe = models.ForeignKey(to=Cafe, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review = models.TextField()


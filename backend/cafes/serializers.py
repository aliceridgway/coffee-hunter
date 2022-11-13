from rest_framework import serializers
from cafes import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class CafeSerializer(serializers.ModelSerializer):

    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=models.Tag.objects.all()
    )

    class Meta:
        model = models.Cafe
        fields = ["id", "name", "address", "website", "tags"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ["id", "title", "rating", "review", "cafe"]

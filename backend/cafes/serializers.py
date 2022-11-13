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

    def validate(self, attrs):
        request = self.context.get("request")
        view = self.context.get("view")
        cafe = attrs.get("cafe")

        if cafe.owner == request.user:
            raise serializers.ValidationError("Owners cannot review own cafe.")

        if (
            models.Review.objects.filter(cafe=cafe, author=request.user).exists()
            and view.action == "create"
        ):
            raise serializers.ValidationError(
                "Only one review per cafe per person allowed."
            )

        return super().validate(attrs)

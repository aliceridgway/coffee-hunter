from rest_framework import serializers

from accounts.models import CustomUser, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["url", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["url", "first_name", "last_name", "profile_picture"]

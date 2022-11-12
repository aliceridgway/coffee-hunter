from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        is_staff: bool = False,
        is_superuser: bool = False,
    ):

        user = CustomUser(username=username, email=email)
        user.set_password(password)

        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        user.save()

        Profile.objects.create(user=user)

        return user

    def create_superuser(self, username: str, email: str, password: str):

        return self.create_user(
            username, email, password, is_staff=True, is_superuser=True
        )


class CustomUser(AbstractUser):
    manager = CustomUserManager()


class ProfileManager(models.Manager):
    def create(self, **kwargs):
        return super().create(**kwargs)


class Profile(models.Model):

    objects = ProfileManager()

    user = models.OneToOneField(
        to=CustomUser, related_name="profile", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)

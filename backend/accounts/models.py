from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str):

        user = CustomUser(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, username: str, email: str, password: str):

        user = CustomUser(
            username=username,
            email=email
        )
        user.set_password(password)

        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user
class CustomUser(AbstractUser):
    manager = CustomUserManager()

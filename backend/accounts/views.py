from rest_framework import mixins
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from accounts.serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from accounts.permissions import ProfilePermission, UserPermission
from backend.permissions import IsOwnerOrReadOnly

from accounts.models import Profile


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = get_user_model().objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [
        UserPermission,
    ]


class ProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [
        ProfilePermission,
    ]

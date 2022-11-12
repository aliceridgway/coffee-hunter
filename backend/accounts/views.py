from rest_framework import viewsets
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model
from accounts.permissions import UserPermission
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
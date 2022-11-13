from backend.permissions import IsOwnerOrReadOnly

from cafes.models import Tag, Cafe, Review
from cafes import serializers

from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet


class TagViewSet(ModelViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class CafeViewSet(ModelViewSet):
    serializer_class = serializers.CafeSerializer
    queryset = Cafe.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewViewSet(ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (permissions.AllowAny,)

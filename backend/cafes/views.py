from backend.permissions import IsOwnerOrReadOnly

from cafes.models import Tag, Cafe, Review
from cafes import permissions as cafe_permissions
from cafes import serializers

from rest_framework import mixins
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet


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


class ReviewViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = serializers.ReviewSerializer
    queryset = Review.objects.select_related("author").all()
    permission_classes = (cafe_permissions.ReviewPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from backend.permissions import IsOwnerOrReadOnly

from cafes.models import Tag, Cafe, Review
from cafes import permissions as cafe_permissions
from cafes import serializers

from rest_framework import mixins
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class TagViewSet(ModelViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class CafeViewSet(ModelViewSet):
    serializer_class = serializers.CafeSerializer
    queryset = Cafe.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    filterset_fields = ["tags"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["GET"])
    def reviews(self, request, pk):
        """
        Gets reviews for a single cafe.
        """
        reviews = (
            Review.objects.select_related("author", "author__profile")
            .filter(cafe_id=pk)
            .order_by("-created_at")
        )
        page = self.paginate_queryset(reviews)

        if page is not None:
            serializer = serializers.ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


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

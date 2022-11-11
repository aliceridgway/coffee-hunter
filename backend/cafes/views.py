
from cafes import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from cafes import models


class TagViewSet(ModelViewSet):
    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects.all()
    permission_classes = (permissions.AllowAny,)


class CafeViewSet(ModelViewSet):
    serializer_class = serializers.CafeSerializer
    queryset = models.Cafe.objects.all()
    permission_classes = (permissions.AllowAny,)
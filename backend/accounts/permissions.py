from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request

from django.db import models


class UserPermission(permissions.BasePermission):
    """
    source: https://stackoverflow.com/questions/19313314/django-rest-framework-viewset-per-action-permissions
    """

    def has_permission(self, request: Request, view: GenericAPIView) -> bool:

        if view.action == "create":
            return True
        elif view.action in ["list", "destroy"]:
            return request.user.is_authenticated and request.user.is_staff
        elif view.action in ["retrieve", "update", "partial_update"]:
            return True  # defer to has_object_permission
        else:
            return False

    def has_object_permission(
        self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        if not request.user.is_authenticated:
            return False

        if view.action in ["retrieve", "update", "partial_update"]:
            return obj == request.user or request.user.is_staff
        elif view.action == "destroy":
            return request.user.is_staff
        else:
            return False


class ProfilePermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        elif view.action in ["retrieve", "update", "partial_update"]:
            return True

        elif view.action == "list":
            return request.user.is_staff

        else:
            return False

    def has_object_permission(self, request, view, obj):

        if view.action == "retrieve":
            return True
        elif view.action in ["update", "partial_update"]:
            return obj.user == request.user or request.user.is_staff
        else:
            return False

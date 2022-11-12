from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request


class UserPermission(permissions.BasePermission):
    """
    source: https://stackoverflow.com/questions/19313314/django-rest-framework-viewset-per-action-permissions
    """
    def has_permission(self, request: Request, view: GenericAPIView) -> bool:
        
        if view.action == "create":
            return True
        elif view.action in ["list", "destroy"]:
            return request.user.is_authenticated and request.user.is_admin
        elif view.action in ["retrieve", "update", "partial_update"]:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        
        if not request.user.is_authenticated:
            return False
        
        if view.action in ["retrieve", "update", "partial_update"]:
            return obj == request.user or obj == request.user.is_admin
        elif view.action == "destroy":
            return obj == request.user.is_admin
        else:
            return False
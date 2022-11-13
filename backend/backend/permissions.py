from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.

    source: https://devdocs.io/django_rest_framework/api-guide/permissions/index#djangomodelpermissions
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`
        is_user = getattr(obj, "user", False)
        is_owner = getattr(obj, "owner", False)

        return is_user or is_owner


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if view.action in ["list", "retrieve"]:
            return True

        return request.user.is_staff

    def has_object_permission(self, request, view, obj):

        if view.action == "retrieve":
            return True

        return request.user.is_staff

from rest_framework import permissions


class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if view.action in ["list", "retrieve"]:
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if view.action == "destroy":
            return request.user.is_staff or obj.author == request.user

        elif view.action == "retrieve":
            return True

        else:
            return False

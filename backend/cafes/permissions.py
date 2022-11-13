from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CanLeaveReview(BasePermission):
    def has_permission(self, request, view):

        if view.action == "create":
            return request.user.is_authenticated
        else:
            return True

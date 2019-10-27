"""Users permissions."""
from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """User permissions."""

    SAFE_METHODS = ("GET", "HEAD", "OPTIONS", "POST")

    def has_object_permission(self, request, view, obj) -> bool:
        """Check user permission."""
        if request.method in self.SAFE_METHODS:
            return True
        return request.user == obj

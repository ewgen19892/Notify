"""Notifications permissions."""
from rest_framework import permissions


class NotificationPermission(permissions.BasePermission):
    """Notification permissions."""

    SAFE_METHODS = ("GET", "HEAD", "OPTIONS",)

    def has_object_permission(self, request, view, obj) -> bool:
        """Check notification permission."""
        user = request.user
        if request.method in self.SAFE_METHODS and user in obj.recipients.all():
            return True
        return user == obj.owner

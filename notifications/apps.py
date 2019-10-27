"""Notifications apps."""
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """Notifications app config."""

    name = "notifications"

    def ready(self):
        """Ready app."""
        import notifications.signals.notifications  # noqa

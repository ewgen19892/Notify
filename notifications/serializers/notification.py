"""Notification serializers."""
from datetime import datetime

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from notifications.models import Notification
from rest_framework import serializers
from users.serializers import UserSerializer


class NotificationSerializer(serializers.ModelSerializer):
    """Notification serializer."""

    class Meta:
        """Meta."""

        fields = [
            "id",
            "owner",
            "title",
            "description",
            "place",
            "recipients",
            "create_at",
            "date",
            "completed",
        ]
        model = Notification
        read_only_fields = (
            "owner",
        )

    def validate_date(self, date) -> datetime:
        """
        Validate date.

        :param date:
        :return:
        """
        now = datetime.now(tz=timezone.utc)
        if now > date:
            raise serializers.ValidationError(
                _("Notification date can't be earlier than current.")
            )
        return date

    def to_representation(self, instance) -> dict:
        """Transform object."""
        self.fields["owner"] = UserSerializer()
        self.fields["recipients"] = UserSerializer(many=True)
        return super().to_representation(instance)

"""Notification filters."""
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from django_filters import rest_framework as filters
from notifications.models import Notification


class NotificationFilter(filters.FilterSet):
    """Notification filters."""

    owner = filters.CharFilter(
        help_text=_("Get my notifications"),
        method="get_owner_notification",
    )
    recipient = filters.CharFilter(
        help_text=_("Get notifications in which I'm recipient"),
        method="get_notification_recipient",
    )

    class Meta:
        """Meta."""

        model = Notification
        fields = ("recipient", "owner")

    def get_owner_notification(self, queryset, name, value) -> QuerySet:
        """
        Filter queryset by owner.

        :param queryset:
        :param name:
        :param value:
        :return:
        """
        del name
        if value:
            return queryset.filter(owner_id=self.request.user.id)
        return queryset

    def get_notification_recipient(self, queryset, name, value) -> QuerySet:
        """
        Filter queryset by recipients.

        :param queryset:
        :param name:
        :param value:
        :return:
        """
        del name
        if value:
            return queryset.filter(recipients__id=self.request.user.id)
        return queryset

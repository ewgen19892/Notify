"""Notification views."""
from django.db.models import Q, QuerySet

from django_filters.rest_framework import DjangoFilterBackend
from notifications.filters import NotificationFilter
from notifications.models import Notification
from notifications.permissions import NotificationPermission
from notifications.serializers import NotificationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class NotificationList(GenericAPIView, ListModelMixin, CreateModelMixin):
    """Notification list view."""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_class = NotificationFilter

    def get_queryset(self) -> QuerySet:
        """
        Get queryset.

        :return: Filtered queryset
        """
        user = self.request.user
        queryset = Notification.objects.filter(
            Q(owner_id=user.id) | Q(recipients__id=user.id)
        ).distinct()
        return queryset

    def get(self, request, *args, **kwargs) -> Response:
        """Get notifications list."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        """Create a new notification."""
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer) -> None:
        """
        Perform create notification.

        :param serializer:
        :return: None
        """
        serializer.save(owner=self.request.user)


class NotificationDetail(
        GenericAPIView,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
):
    """Notification detail view."""

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = (IsAuthenticated, NotificationPermission)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get notification.

        Get notification by ID.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        """
        Partial notification update.

        Partial notification update with this id.
        """
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> Response:
        """
        Delete notification.

        Destroy a notification instance.
        """
        return self.destroy(request, *args, **kwargs)

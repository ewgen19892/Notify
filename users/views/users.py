"""Users views."""
from django.contrib.auth.models import User

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserList(GenericAPIView, ListModelMixin, CreateModelMixin):
    """User list view."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get users list.

        Get all existing users.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        """
        Register user with credentials.

        Register a new user in the app.
        """
        return self.create(request, *args, **kwargs)


class UserDetail(
        GenericAPIView,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
):
    """User detail view."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, UserPermission,)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Get user.

        Get user by ID.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        """
        Partial user update.

        Partial user update with this id.
        """
        return self.partial_update(request, *args, **kwargs)

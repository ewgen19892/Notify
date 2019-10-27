"""Users serializers."""
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    def validate_password(self, password) -> str:
        """Validate password."""
        validate_password(password)
        if self.instance is None:
            return password
        return make_password(password)

    def create(self, validated_data) -> User:
        """Create user."""
        return User.objects.create_user(**validated_data)

    class Meta:
        """Meta."""

        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "email",
            "username",
        ]
        model = User
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
            "email": {
                "required": True,
            },
        }

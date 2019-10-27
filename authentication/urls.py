"""Authentication URL Configuration."""
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "authentication"

urlpatterns = [
    path("auth/token/", TokenObtainPairView.as_view(), name="obtain_token"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]

"""Notify URL Configuration."""

from django.contrib import admin
from django.urls import include, path

from notify.views import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0),
         name="documentation"),
    path("", include("users.urls")),
    path("", include("notifications.urls")),
    path("", include("authentication.urls")),
]

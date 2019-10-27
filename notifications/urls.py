"""Notifications URL Configuration."""
from django.urls import path

from notifications.views import NotificationDetail, NotificationList

app_name = "notifications"
urlpatterns = [

    path("notifications/", NotificationList.as_view(), name="notification_list"),
    path("notifications/<slug:pk>/", NotificationDetail.as_view(),
         name="notification_detail"),

]

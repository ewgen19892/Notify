"""Users URL Configuration."""
from django.urls import path

from users.views import UserDetail, UserList

app_name = "users"
urlpatterns = [

    path("users/", UserList.as_view(), name="user_list"),
    path("users/<slug:pk>/", UserDetail.as_view(), name="user_detail"),

]

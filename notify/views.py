"""Notify views."""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from notify import __version__
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Notify API",
        default_version=__version__,
        description="Backend",
        contact=openapi.Contact(
            name="Bakhauchuk Yauhen",
            email="e.bohovchuk@gmail.com",
        ),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated,),
    authentication_classes=(
        JWTAuthentication,
        SessionAuthentication,
    ),
)

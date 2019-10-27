"""Notify docs."""
from drf_yasg import openapi
from drf_yasg.inspectors import PaginatorInspector


class NotifyPaginatorInspector(PaginatorInspector):
    """Notify paginator inspector."""

    def get_paginator_parameters(self, paginator):
        """Get paginator query parameters."""
        return [
            openapi.Parameter(
                name="page_size",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Number of items per page",
                default=6,
            ),
            openapi.Parameter(
                name="page",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number",
                default=1,
            ),
        ]

    def get_paginated_response(self, paginator, response_schema):
        """Get paginated schema."""
        return response_schema

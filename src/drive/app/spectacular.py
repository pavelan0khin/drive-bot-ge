from django.urls import path
from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


class ExcludeFromSchemaMixin:
    @extend_schema(exclude=True)
    def get(self, request):
        return super().get(request)


class CustomSpectacularAPIView(ExcludeFromSchemaMixin, SpectacularAPIView):
    pass


patterns = [
    path(
        "api/v1/openapi.yaml/",
        CustomSpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/v1/openapi/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="openapi",
    ),
    path(
        "api/v1/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from drive.exam.views.api import v1 as v1_views

from .spectacular import patterns as schema_patterns

v1_router = SimpleRouter()

v1_router.register("ticket", v1_views.TicketViewSet)
v1_router.register("category", v1_views.CategoryViewSet)
v1_router.register("answer", v1_views.AnswerViewSet)
v1_router.register("topic", v1_views.TopicViewSet)
v1_router.register("image", v1_views.ImageViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("bot/", include("drive.bot.urls")),
    path("exam/", include("drive.exam.urls")),
    path("api/v1/", include(v1_router.urls)),
]

urlpatterns += schema_patterns

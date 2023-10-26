from django.urls import path

from drive.bot import views

urlpatterns = [
    path("set-webhook/", views.set_webhook),
    path("new-update/", views.new_update),
]

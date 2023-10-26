from django.urls import path

from drive.exam import views

urlpatterns = [path("ticket/<int:pk>/description/<str:lang>/", views.ticket_description)]

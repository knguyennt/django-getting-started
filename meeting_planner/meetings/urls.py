from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('room_listing', views.room_listing, name='room_listing'),
    path("new", views.new, name="new_meeting")
]
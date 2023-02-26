from django.urls import path
from app_mascota import views

urlpatterns = [
    path('',views.inicio),
    path('mascota', views.mascota, name="Mascota"),
]
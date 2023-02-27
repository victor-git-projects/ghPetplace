from django.urls import path
from app_mascota import views

urlpatterns = [
    path('',views.base, name = "Origin"),
    path('mascota', views.mascota, name="Mascota"),
]
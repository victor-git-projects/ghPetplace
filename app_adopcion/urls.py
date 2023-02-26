from django.urls import path
from app_adopcion import views

urlpatterns = [
    path('',views.inicio),
    path('adopcion', views.adopcion, name="Adopcion"),
]
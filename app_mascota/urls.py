from django.urls import path
from app_mascota import views

urlpatterns = [
    path('',views.base, name = "Origin"),
    path('mascota/', views.mascota, name="Mascota"),
    path('mascotaform/', views.mascota_view, name="Mascotaform"),
    path('mascotalist/', views.mascota_list, name="Mascotalist"),
    path('mascotaedit/<id_mascota>', views.mascota_edit, name="Mascotaedit"),
    path('mascotadelete/<id_mascota>', views.mascota_delete, name="Mascotadelete"),
]
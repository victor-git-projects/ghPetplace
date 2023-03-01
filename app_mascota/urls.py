from django.urls import path
from app_mascota import views
from app_mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('',views.base, name = "Origin"),
    path('mascota/', views.mascota, name="Mascota"),
    
    #Aca es mi lista pero se llama basado en funciones pero ahora abajo la estoy colocando como vista por clase.
    #path('mascotaform/', views.mascota_view, name="Mascotaform"),
    path('mascotaform/', MascotaCreate.as_view(), name="Mascotaform"),
    
    #Aca es mi lista pero se llama basado en funciones pero ahora abajo la estoy colocando como vista por clase.
    #path('mascotalist/', views.mascota_list, name="Mascotalist"),
    path('mascotalist/', MascotaList.as_view(), name="Mascotalist"),
    
    #path('mascotaedit/<id_mascota>', views.mascota_edit, name="Mascotaedit"),
    path('mascotaedit/<pk>', MascotaUpdate.as_view(), name="Mascotaedit"),
    
    
    #path('mascotadelete/<id_mascota>', views.mascota_delete, name="Mascotadelete"),
    path('mascotadelete/<pk>', MascotaDelete.as_view(), name="Mascotadelete"),
]
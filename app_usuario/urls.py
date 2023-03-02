from django.urls import path

from app_usuario import views
from app_usuario.views import UsuarioRegister


urlpatterns = [
    path('',views.base, name = "Origin"),
    path('usuarioregister/', UsuarioRegister.as_view(), name="Usuarioregister"),
    
]
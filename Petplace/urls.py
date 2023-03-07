"""Petplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
#from app_mascota.views import mascota
#from app_adopcion.views import adopcion
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('mascota/', mascota ),
    #path('adopcion/', adopcion ),
    path('app_mascota/', include('app_mascota.urls')),
    path('app_adopcion/', include('app_adopcion.urls')),
    path('app_usuario/', include('app_usuario.urls')),
    path('home/', LoginView.as_view(template_name = 'index.html'), name="Home"),
    
]

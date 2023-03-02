from django.urls import path
from app_adopcion import views
from app_adopcion.views import SolicitudList, SolicitudCreate, SolicitudEdit, SolicitudDelete


urlpatterns = [
    path('',views.base, name='Origin'),
    path('adopcion/', views.adopcion, name="Adopcion"),
    path('solicitudlist/', SolicitudList.as_view(), name="Solicitudlist"),
    path('solicitudcreate/', SolicitudCreate.as_view(), name="Solicitudcreate"),
    path('solicitudedit/<pk>', SolicitudEdit.as_view(), name="Solicitudedit"),
    path('solicituddelete/<pk>', SolicitudDelete.as_view(), name="Solicituddelete"),
]
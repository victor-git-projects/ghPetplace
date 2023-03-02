from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from app_usuario.forms import RegistroForm

# Create your views here.

def base (request):
    return render(request,'base/base.html')
    

class UsuarioRegister(CreateView):
    model = User
    template_name = "usuario/usuario_register.html"
    form_class = RegistroForm
    success_url = reverse_lazy('Mascotalist')
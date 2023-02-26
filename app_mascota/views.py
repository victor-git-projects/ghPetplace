from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def inicio (request):
    return HttpResponse("Esta es la vista inicio pero de mascotas")

def mascota (request):
    return HttpResponse("Esta es la vista de mascotas")

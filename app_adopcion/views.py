from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Este es el inicio de adopcion")

def adopcion(request):
    return HttpResponse("Esta es la vista de adopcion")
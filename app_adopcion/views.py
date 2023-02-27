from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#def inicio(request):
#   return HttpResponse("Este es el inicio de adopcion")

def base(request):
    return render(request, 'base/base.html')
    #return HttpResponse("Esta es la vista de adopcion")

def adopcion(request):
    return render(request, 'adopcion/index.html')
    #return HttpResponse("Esta es la vista de adopcion")
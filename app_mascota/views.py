from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#def inicio (request):
#    return HttpResponse("Esta es la vista inicio pero de mascotas")

def base (request):
    return render(request,'base/base.html')
    #return HttpResponse("Esta es la vista de mascotas")


def mascota (request):
    return render(request,'mascota/index.html')
    #return HttpResponse("Esta es la vista de mascotas")

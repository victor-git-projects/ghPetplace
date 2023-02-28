from django.shortcuts import render, redirect

from django.http import HttpResponse

from app_mascota.forms import MascotaForm

# Create your views here.

#def inicio (request):
#    return HttpResponse("Esta es la vista inicio pero de mascotas")

def base (request):
    return render(request,'base/base.html')
    #return HttpResponse("Esta es la vista de mascotas")


def mascota (request):
    return render(request,'mascota/index.html')
    #return HttpResponse("Esta es la vista de mascotas")
    
def mascota_view (request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Origin')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})
            

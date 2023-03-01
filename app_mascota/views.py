from django.shortcuts import render, redirect

from django.http import HttpResponse

from app_mascota.forms import MascotaForm
from app_mascota.models import Mascota

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

#def inicio (request):
#    return HttpResponse("Esta es la vista inicio pero de mascotas")

def base (request):
    return render(request,'base/base.html')
    #return HttpResponse("Esta es la vista de mascotas")


def mascota (request):
    return render(request,'mascota/index.html')
    #return HttpResponse("Esta es la vista de mascotas")
    
#def mascota_view (request):
#    if request.method == 'POST':
#        form = MascotaForm(request.POST)
#        if form.is_valid():
#            form.save()
#        return redirect('Origin')
#    else:
#        form = MascotaForm()
#    return render(request, 'mascota/mascota_form.html', {'form': form})


### Aca voy hacer una lista en mascota pero esto es una vista por medio de funcion, abajo active la vista por medio de clase entonces esto ya no seria necesario
#def mascota_list (request):
#    mascota = Mascota.objects.all().order_by('id')
#    contexto = {'mascota':mascota}
#    return render(request, 'mascota/mascota_list.html', contexto)

### Aca voy a definir una funcion para eliminar y otra para editar, tener en cuenta que vamos a recibir un id de mascota

## lo acabo de desabilitar porque lo he puesto como clase es la UpdateView que hace el tema de editar en vez de funciones
#def mascota_edit(request, id_mascota):
#    mascota = Mascota.objects.get(id=id_mascota)
#    if request.method == 'GET':
#        form = MascotaForm(instance=mascota)
#    else:
#        form = MascotaForm(request.POST, instance=mascota)
#        if form.is_valid():
#            form.save()
#        return redirect('Mascotalist')
#    return render(request, 'mascota/mascota_form.html', {'form':form})


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('Mascotalist')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})


## Aca voy hacer una vista basada en clase ya no en funcion, ojo debo de importar el ListView de Django
            
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    
class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('Mascotalist')
    
class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('Mascotalist')
    
class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('Mascotalist')

from django.db import models
from app_adopcion.models import Persona  #Esto es para el atributo de uno a muchos

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)


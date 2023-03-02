from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    
    
    #con esto me va devolver el nombre ya que me estaba devolviendo las cosas como objetos
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)
    
    
## Empiezo con la creacion de CRUD con dos formularios

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    

    

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=10)
    conductor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.placa

class Distrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre       

class Favoritos(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.direccion

class Viaje(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    distrito_recojo = models.ForeignKey(Distrito, related_name='recojo',on_delete=models.CASCADE)
    direccion_recojo = models.CharField(max_length=100)
    distrito_destino = models.ForeignKey(Distrito, related_name='destino', on_delete=models.CASCADE)
    direccion_detino = models.CharField(max_length=100)dir
    fecha_hora_solicitado = models.DateTimeField(auto_now_add=True)
    fecha_hora_atendido = models.DateTimeField(null=True, blank=True)
    fecha_hora_terminado = models.DateTimeField(null=True, blank=True)
    puntos_valoracion = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    estado = models.CharField(max_length=1)
    
    #def __str__(self):
    #   return self.marca.nombre

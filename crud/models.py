from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.

class Tablero(models.Model):
    encargado = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    creado = models.DateTimeField(default=timezone.now)
    estado = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.titulo} de {self.encargado}'

class Lista(models.Model):
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, blank=False, null=False)
    def __str__(self):
        return {self.tablero}







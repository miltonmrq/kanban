from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class Tablero(models.Model):
    titulo = models.CharField(max_length=255, blank=False, null=False)
    
    
    def __str__(self):
        return f'{self.titulo}'


    
class Tarea(models.Model):
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, unique=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    creado = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=one_week_hence)
    def __str__(self):
        return f'{self.titulo} {self.descripcion}'


    

from django.db import models

# Create your models here.

class Actividad(models.Model):
    descripcion = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    def __str__(self):
        return "%s %s" % (self.descripcion, self.estado)






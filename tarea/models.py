# models.py

from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre




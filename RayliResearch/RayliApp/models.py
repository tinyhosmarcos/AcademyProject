from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre          = models.CharField(max_length=100)
    descripcion     = models.TextField()
    precio          = models.FloatField()
    fecha_inicio    = models.DateField()
    fecha_fin       = models.DateField()
    cupos_habiles   = models.IntegerField()

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre          = models.CharField(max_length=100)
    descripcion     = models.TextField()
    contacto        = models.IntegerField()
    email           = models.EmailField()
    def __str__(self):
        return self.nombre

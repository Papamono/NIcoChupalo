from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length = 20)
    clave = models.CharField(max_length = 20)
    correo = models.EmailField(max_length = 50)


class Mascotas(models.Model):

    fotografia = models.ImageField(upload_to = "Imagenes/")
    nombre_mascota = models.CharField(max_length = 20)
    raza_predominante = models.CharField(max_length = 20)
    descripcion = models.TextField()
    estado = models.CharField(max_length = 20)

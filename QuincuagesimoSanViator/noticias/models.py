from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Noticia(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen",upload_to="Noticias")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title



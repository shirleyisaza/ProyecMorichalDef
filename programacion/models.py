from django.db import models

# Create your models here.
class Programacion(models.Model):
    nombre_categoria=models.CharField(max_length=45, verbose_name="Categoria")
    horario=models.CharField(max_length=45, verbose_name="Horario")
    estado=models.CharField(max_length=45, verbose_name="Estado")
    def __str__(self):
        return self.horario
    
    
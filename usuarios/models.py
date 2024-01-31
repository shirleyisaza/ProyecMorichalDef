from django.db import models

# Create your models here.
class Usuario(models.Model):
        nombre= models.CharField(max_length=50, verbose_name='Nombre')
        nombre= models.CharField(max_length=50, verbose_name='Apellido')
        documento= models.CharField(unique=True, max_length=10)
        
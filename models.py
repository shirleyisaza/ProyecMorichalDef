from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Usuario(models.Model):
    class Estado(models.charfield):
        nombre= models.CharField(max_length=50, verbose_name='Nombre')
        nombre= models.CharField(max_length=50, verbose_name='Apellido')
        documento= models.CharField(unique=True, max_length=10)
        Activo = '1', _('Activo')
        Inactivo = '0', _('Inativo')
        
        def __str__(self) ->str:
            return "%s %s" %(self.nombre, self.apellido)
        
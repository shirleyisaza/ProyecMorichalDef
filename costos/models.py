from django.db import models
from django.utils.translation import gettext_lazy as _

class Costos(models.Model):
    concepto = models.CharField(max_length=45, verbose_name="concepto_costos")
    
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
        
def __str__(self):
    return "%s %s" %(self.nombres, self.apellidos)
        
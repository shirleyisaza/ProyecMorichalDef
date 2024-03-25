from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Deportista(models.Model):
    genero = models.TextField(max_length=45, verbose_name="Genero")
    lugar_nacimiento = models.TextField(max_length=45, verbose_name="Lugar de Nacimiento")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", help_text="MM/DD/AAAA")
    edad = models.IntegerField(verbose_name="Edad")
    peso = models.IntegerField(verbose_name="Peso en Kg")
    estatura = models.IntegerField(verbose_name="Estatura")
    ciudad = models.TextField(max_length=45, verbose_name="Ciudad")
    barrio = models.TextField(max_length=45, verbose_name="Barrio")
    direccion = models.TextField(max_length=45, verbose_name="Direccion")
    eps = models.TextField(max_length=45, verbose_name="Eps")
    
    class Estado(models.TextChoices):
        ACTIVO = '1', _('SI')
        INACTIVO = '0', _('NO')
    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado Activo?")
    
    def __str__(self):
        return self.genero
from django.db import models
from django.utils.translation import gettext_lazy as _
from programacion.models import Programacion


# Create your models here.
class Deportista(models.Model):
    genero = models.TextField(max_length=45, verbose_name="Genero")
    lugarNacimiento = models.TextField(max_length=45, verbose_name="Lugar de Nacimiento")
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento", help_text="MM/DD/AAAA")
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


    estado = models.CharField(max_length=2, choices=Estado.choices, default="Estado.ACTIVO", verbose_name="Estado Activo")
    
    def __str__(self) -> str:
        return self.genero
    
class Reporte_pago(models.Model):
    mes_pago=models.CharField(max_length=255)
    Reporte_pago=models.ImageField(upload_to='imagenes/')
    
    def __str__(self) -> str:
        return self.mes_pago
    
class Deportista_programa(models.Model):
    programacion= models.ForeignKey(Programacion, verbose_name="Programa",  on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.Programacion

    
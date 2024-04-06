from django.utils.translation import gettext_lazy as _
from django.db import models

    
class Sucursal(models.Model):
    nombre=models.TextField(max_length=80, verbose_name='Nombre Sucursal')
    empresa=models.ForeignKey(Empresa, on_delate=models.CASCADE, verbose_name='Club_Deportivo_Morichal')
    direccion=models.CharField(max_length=70, verbose_name='Direccion')
    Telefono=models.CharField(max_length=20, verbose_name='Telefono', blank=True)
    administrador=models.ForeignKey('Usuario', on_delate=models.CASCADE, verbose_name='Administrador')
    municipio=models.ForeignKey(Municipio, on_delate=models.CASCADE, verbose_name='Municipio')
    class Estado(models.Model): 
            ACTIVO='1', _('Activo')
            INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, Choices=Estado.Choices, default=Estado.Activo, verbose_name='Estado')
           
    

class Usuario(models.Model):
    class Estado(models.charfield):
        nombre= models.CharField(max_length=50, verbose_name='Nombre')
        apellidos= models.CharField(max_length=50, verbose_name='Apellidos')
        
        class TipoDocumento(models.Model): 
            CC='C.C', _('Cedula de Ciudadania')
            RC='R.C', _('Registro Civil')
            TI='T.I', _('Tarjeta de Identidad')
        tipodocumento=models.CharField(max_length=4, Choices=TipoDocumento.Choices, default=TipoDocumento.CC,verbose_name='tipo de documento')
        documento=models.CharField(max_length=50, verbose_name='numero de documento')
        Fecha_Registro=models.DateField(verbose_name="fecha de nacimiento", help_text=u"MM/DD/AAAA")
       
        class Rol(models.Model): 
            administracion= 'Administrador', _('Administrador')
            Entrenador= 'Entrenador', _('Entrenador')
            Deportista= 'Deportista', _('Deportista')
        rol=models.CharField(max_length=13, Choices=Rol.Choices, default=Rol.Deportista, verbose_name='Rol')
        sucursal=models.CharField(Sucursal, on_delate=models.CASCADE, verbose_name='sucursal')
        class Estado(models.Model): 
            ACTIVO='1', _('Activo')
            INACTIVO='0', _('Inactivo')
        estado=models.CharField(max_length=1, Choices=Estado.Choices, default=Estado.Activo, verbose_name='Estado')
        
       
       
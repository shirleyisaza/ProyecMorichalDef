from django.db import models


class Usuario(models.Model):
    nombre= models.CharField(max_length=50, verbose_name="Nombre")
    apellido= models.CharField(max_length=50, verbose_name="Apellido")
    documento= models.CharField(unique=True, max_length=10)

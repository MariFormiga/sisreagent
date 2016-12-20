from django.db import models
from django.utils import timezone


class Armazenamento(models.Model):
    Tipo_de_armazenamento = models.CharField(max_length=200)
    CNPJ = models.CharField(max_length=200)
    Subtipo_de_armazenamento = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Armazenamento'




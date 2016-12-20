from django.db import models
from django.utils import timezone


class Vidraria(models.Model):
    vidraria = models.CharField(max_length=200)
    Quantidade_Disponivel = models.CharField(max_length=200)

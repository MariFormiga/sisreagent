from django.db import models
from django.utils import timezone

class Pratica (models.Model):
    Pratica = models.CharField(max_length=200)
    Grupo = models.CharField(max_length=200)
    Professor_Responsavel = models.CharField(max_length=200)
    Material = models.CharField(max_length=200)
    Tema = models.CharField(max_length=200)
    
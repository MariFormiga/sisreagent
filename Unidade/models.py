from django.db import models
from django.utils import timezone

class Unidade(models.Model):
    Unidade = models.CharField(max_length=200)
    Sigla = models.CharField(max_length=200)

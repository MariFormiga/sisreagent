from django.db import models
from django.utils import timezone

class Periodo (models.Model):
    Periodo = models.CharField(max_length=200)
    Disciplina = models.CharField(max_length=200)

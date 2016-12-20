from Reagente.models import Reagente
from Vidraria.models import Vidraria
from django.db import models
from django.utils import timezone


class Baixa(models.Model):
    Produto = models.ForeignKey(Vidraria)



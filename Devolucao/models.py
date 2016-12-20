from Reagentes.models import Reagente
from django.db import models
from django.utils import timezone
from Unidade.models import Unidade
from Vidraria.models import Vidraria

class Devolucao(models.Model):
    Reagente = models.ForeignKey(Reagente)
    Vidraria = models.ForeignKey(Vidraria)
    Quantidade = models.CharField(max_length=200)
    Unidade = models.ForeignKey(Unidade)

    class Meta:
        verbose_name_plural = 'Devolucao'

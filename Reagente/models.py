from django.db import models
from django.utils import timezone
from Unidade.models import Unidade
from Armazenamento.models import Armazenamento

class Reagente (models.Model):
    Produto = models.CharField(max_length=200)
    Grau_de_Pureza = models.CharField(max_length=200)
    Valor_Comercial = models.CharField(max_length=200)
    Classe = models.CharField(max_length=200)
    Tipo_de_Armazenamento = models.ForeignKey(Armazenamento)
    Quantidade_Disponivel = models.CharField(max_length=200)
    Validade = models.DateField()
    Unidade = models.ForeignKey(Unidade)

    class Meta:
        verbose_name_plural = 'Reagente'

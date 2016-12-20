from django.db import models
from django.utils import timezone
from Unidade.models import Unidade
from Reagente.models import Reagente
from Periodo.models import Periodo
from Fornecedores.models import Fornecedores
from Vidraria.models import Vidraria

class Controle_de_Validade(models.Model):
    Descricao = models.CharField(max_length=200)
    Ordenar = models.CharField(max_length=200)
    Dias = models.CharField(max_length=200)
    Validade = models.DateField()


class Ficha_Cardex(models.Model):
    Reagente = models.ForeignKey(Reagente)
    Periodo = models.DateField()


class Itens(models.Model):
    Descricao = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Itens'


class Devolucao_de_Produtos(models.Model):
    Pratica = models.CharField(max_length=200)
    Unidade = models.ForeignKey(Unidade)
    Periodo = models.ForeignKey(Periodo)
    class Meta:
        verbose_name_plural = 'Devolucao_de_Produtos'


class Livro_de_Registro(models.Model):
    Reagente = models.ForeignKey(Reagente)
    Vidraria = models.ForeignKey(Vidraria)
    Data_de_Inicio = models.DateField()
    Data_Final = models.DateField()
    Unidade = models.ForeignKey(Unidade)


class Ultimas_Compras(models.Model):
    Reagente = models.ForeignKey(Reagente)
    Vidraria = models.ForeignKey(Vidraria)
    Data_de_Inicio = models.DateField()
    Data_Final = models.DateField()
    Unidade = models.ForeignKey(Unidade)
    class Meta:
        verbose_name_plural = 'Ultimas_Compras'


class Fornecedores(models.Model):
    Fornecedores = models.ForeignKey(Fornecedores)
    class Meta:
        verbose_name_plural = 'Fornecedores'








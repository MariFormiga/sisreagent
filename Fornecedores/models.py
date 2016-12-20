from django.db import models
from django.utils import timezone


class Fornecedores (models.Model):
    Nome_Fantasia = models.CharField(max_length=200)
    CNPJ = models.CharField(max_length=200)
    Endereço = models.CharField(max_length=200)
    Entrega = models.CharField(max_length=200)
    Atraso = models.CharField(max_length=200)
    Pagamento = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Observação = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = 'Fornecedores'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reagente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto', models.CharField(max_length=200)),
                ('Grau_de_Pureza', models.CharField(max_length=200)),
                ('Valor_Comercial', models.CharField(max_length=200)),
                ('Classe', models.CharField(max_length=200)),
                ('Tipo_de_Armazenamento', models.CharField(max_length=200)),
                ('Quantidade_Disponivel', models.CharField(max_length=200)),
                ('Validade', models.CharField(max_length=200)),
                ('Unidade', models.CharField(max_length=200)),
            ],
        ),
    ]

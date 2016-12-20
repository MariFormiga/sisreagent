# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Nome_Fantasia', models.CharField(max_length=200)),
                ('CNPJ', models.CharField(max_length=200)),
                ('Endereço', models.CharField(max_length=200)),
                ('Entrega', models.CharField(max_length=200)),
                ('Atraso', models.CharField(max_length=200)),
                ('Pagamento', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Observação', models.CharField(max_length=500)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armazenamento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Tipo_de_armazenamento', models.CharField(max_length=200)),
                ('CNPJ', models.CharField(max_length=200)),
                ('Subtipo_de_armazenamento', models.CharField(max_length=200)),
            ],
        ),
    ]

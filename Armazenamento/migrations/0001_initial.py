# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armazenamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_de_armazenamento', models.CharField(max_length=200)),
                ('CNPJ', models.CharField(max_length=200)),
                ('Subtipo_de_armazenamento', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Armazenamento',
            },
        ),
    ]

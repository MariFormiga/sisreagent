# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vidraria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Vidraria', models.CharField(max_length=200)),
                ('Quantidade_Disponivel', models.CharField(max_length=200)),
            ],
        ),
    ]

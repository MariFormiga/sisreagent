from django.db import models
from django.utils import timezone


class Riscos(models.Model):
    Classes = models.CharField(max_length=200)
    Subclasses = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Riscos'

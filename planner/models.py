from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse

class YarnManufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class YarnNumberingSystem(models.Model):
    name = models.CharField(max_length=3, unique=True)
    help = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Yarn(models.Model):
    SETT_UNIT = (
        ('IN', 'yarns/inch'),
        ('CM', 'yarns/cm')
    )
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(YarnManufacturer, on_delete=models.PROTECT)
    material = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    numbering_system = models.ForeignKey(YarnNumberingSystem, on_delete=models.PROTECT)
    sett = models.FloatField()
    sett_unit = models.CharField(max_length=2, choices=SETT_UNIT)

    def get_absolute_url(self):
        return reverse('planner:yarn_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def sett_unit_name(self):
        return dict(Yarn.SETT_UNIT)[self.sett_unit]

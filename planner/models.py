from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Plan(models.Model):
    title_text = models.CharField(max_length=200)

class YarnManufacturer(models.Model):
    name_text = models.CharField(max_length=200)

class Yarn(models.Model):
    manufacturer = models.ForeignKey(YarnManufacturer, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    thickness = models.FloatField()


    

from django.db import models

# Create your models here.

class Abuelo(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField()
    
class Madre(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField()
    
class Hermano(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField()        
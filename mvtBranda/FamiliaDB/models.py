from django.db import models

class Familiar(models.Model):
    
    parentezco = models.CharField(max_length=15)
    nombre = models.CharField(max_length=15)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    
    
class Mascota(models.Model):
    
    nombre = models.CharField(max_length=15)
    especie = models.CharField(max_length=15)
    edad = models.IntegerField()
    
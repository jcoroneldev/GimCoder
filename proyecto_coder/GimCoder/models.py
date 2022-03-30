from pickle import TRUE
from django.db import models

class profesor(models.Model):
    id = models.AutoField(primary_key=TRUE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)

class cliente(models.Model):
    id = models.AutoField(primary_key=TRUE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    peso = models.IntegerField()
    altura = models.IntegerField()

class rutina(models.Model):
    id = models.AutoField(primary_key=TRUE)
    repeticiones = models.IntegerField()
    ejercicio1 = models.CharField(max_length=40)
    ejercicio2 = models.CharField(max_length=40)
    ejercicio3 = models.CharField(max_length=40)
    ejercicio4 = models.CharField(max_length=40)
    ejercicio5 = models.CharField(max_length=40)
    ejercicio6 = models.CharField(max_length=40)

class ejercicio(models.Model):
    id = models.AutoField(primary_key=TRUE)
    nombre = models.CharField(max_length=40)
    detalle = models.CharField(max_length=80)
    demostracion = models.CharField(max_length=40)
    repeticiones = models.IntegerField()
    duracion = models.TimeField()
    



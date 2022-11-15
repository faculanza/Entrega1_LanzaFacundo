from django.db import models

# Create your models here.
class Productos(models.Model):
    producto=models.CharField(max_length=50)
    precio=models.FloatField()
    idcategoria=models.IntegerField()
    idfabrica=models.IntegerField()

class Categorias(models.Model):
    categoria=models.CharField(max_length=50)

class Fabricas(models.Model):
    fabrica=models.CharField(max_length=50)



    
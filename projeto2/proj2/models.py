from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    Quantidade = models.IntegerField()
    descrição = models.CharField(max_length=200)

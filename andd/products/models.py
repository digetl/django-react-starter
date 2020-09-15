from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    price = models.FloatField
    picture = models.ImageField
    quantity = models.IntegerField

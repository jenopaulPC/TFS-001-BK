from django.db import models
import uuid
from .models import *

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products_field')

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    # logo = models.ImageField(upload_to='brands_field', blank=True, null=True)

    def __str__(self):
        return self.name
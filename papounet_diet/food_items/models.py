from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    code = models.CharField(max_length=14, unique=True)
    brand = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    last_modified = models.DateTimeField()
    ingredients = models.TextField()
    energy_kcal = models.IntegerField()
    nutrition_score = models.CharField(max_length=1)
    sugars_100g = models.IntegerField()
    fat_100g = models.IntegerField()
    selection = models.ManyToManyField(User, through='BestProductSelection')

    def __str__(self):
        return self.code


class Store(models.Model):
    name = models.CharField(max_length=280)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=560)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class BestProductSelection(models.Model):
    date_selection = models.DateTimeField()
    code = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


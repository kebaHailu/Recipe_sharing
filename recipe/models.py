from django.db import models
from django.conf import settings

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    preparation_time = models.IntegerField()


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    item_name =  models.CharField(max_length=255)
    quantities = models.DecimalField(max_digits=10, decimal_places=2)

class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

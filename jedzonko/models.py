from django.db import models
from datetime import timezone


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    ingredients = models.CharField(max_length=64)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    preparation = models.IntegerField(null=False)
    votes = models.IntegerField(default=0)
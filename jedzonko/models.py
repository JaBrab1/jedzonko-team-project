from django.db import models
from datetime import *


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateField(auto_now_add=timezone)
    updated = models.DateField(auto_now=timezone)
    preparation = models.IntegerField(null=False)
    votes = models.IntegerField(default=0)


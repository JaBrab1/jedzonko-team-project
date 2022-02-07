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
    method_of_preparation = models.TextField()

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=timezone)
    recipes = models.ManyToManyField(Recipe, through="RecipePlan")


DAY = (
    ("Mondey", "Poniedziałek"),
    ("Tuesday", "Wtorek"),
    ("Wednesday", "Środa"),
    ("Thursday", "Czwartek"),
    ("Friday", "Piątek"),
    ("Saturday", "Sobota"),
    ("Sunday", "Niedziela"),
)


class Dayname(models.Model):
    name = models.CharField(max_length=16, choices=DAY)
    order = models.IntegerField(unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField()
    day_name = models.ForeignKey(Dayname, on_delete=models.CASCADE)


from datetime import datetime
from django.shortcuts import render
from django.views import View
import random

import jedzonko.models
from jedzonko.models import Recipe, Plan


class IndexView(View):
    def get(self, request):
        recpies = list(Recipe.objects.all())
        random.shuffle(recpies)
        ctx = {"actual_date": datetime.now(), "recipe": recpies}
        return render(request, "index.html", ctx)


class Dashboard(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        planes = Plan.objects.all()
        return render(request, "dashboard.html", {'recipes': recipes, 'planes':planes})


class RecipeID(View):
    def get(self, request):
        return render(request, "app-recipe-details.html")


class RecipeList(View):
    def get(self, request):
        return render(request, "app-recipes.html")


class RecipeAdd(View):
    def get(self, request):
        return render(request, "app-add-recipe.html")


class RecipeModify(View):
    def get(self, request):
        return render(request, "app-edit-recipe.html")


class PlanID(View):
    def get(self, request, id):
        plan = Plan.objects.get(id=id)
        return render(request, "app-details-schedules.html", {'plan':plan})


class PlanAdd(View):
    def get(self, request):
        return render(request, "app-add-schedules.html")


class PlanAddRecipe(View):
    def get(self, request):
        return render(request, "app-schedules-meal-recipe.html")


class PlanList(View):
    def get(self, request):
        return render(request, "app-schedules.html")



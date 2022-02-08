from datetime import datetime
from django.shortcuts import render, redirect, render_to_response
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
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
        return render(request, "dashboard.html", {'recipes': recipes, 'planes': planes})


class RecipeID(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        return render(request, "app-recipe-details.html", {"recipe": recipe})


class RecipeList(View):
    def get(self, request):
        return render(request, "app-recipes.html")


class RecipeAdd(View):
    def get(self, request):
        return render(request, "app-add-recipe.html")

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get("description")
        preparation = request.POST.get("preparation")
        method_of_preparation = request.POST.get("method_of_preparation")
        ingredients = request.POST.get("ingredients")
        if name != "" and description != "" and preparation != "" and method_of_preparation != "" and ingredients != "":
            Recipe.objects.create(
                name=name,
                description=description,
                preparation=preparation,
                method_of_preparation=method_of_preparation,
                ingredients=ingredients
            )
            return redirect('/recipe/list/')
        else:
            return render(request, 'app-add-recipe.html', {'alert_flag': True})


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

    def post(self, request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name != "" and description != "":
            Plan.objects.create(name=name, description=description)
            return redirect('/plan/<int:id>/details/')
        else:
            return render(request, 'app-add-schedules.html', {'alert_flag': True})


class PlanAddRecipe(View):
    def get(self, request):
        return render(request, "app-schedules-meal-recipe.html")


class PlanList(View):
    def get(self, request):
        return render(request, "app-schedules.html")



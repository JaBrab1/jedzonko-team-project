from datetime import datetime
from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)


class Dashboard(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "dashboard.html", {'recipes':recipes})

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
    def get(self, request):
        return render(request, "app-details-schedules.html")

class PlanAdd(View):
    def get(self, request):
        return render(request, "app-add-schedules.html")

class PlanAddRecipe(View):
    def get(self, request):
        return render(request, "app-schedules-meal-recipe.html")

class PlanList(View):
    def get(self, request):
        return render(request, "app-schedules.html")
from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
import random
from jedzonko.models import Recipe, Plan, Recipeplan, Dayname
from django.db.models import Count


class IndexView(View):
    def get(self, request):
        recpies = list(Recipe.objects.all())
        random.shuffle(recpies)
        ctx = {"actual_date": datetime.now(), "recipe": recpies}
        return render(request, "index.html", ctx)


class Dashboard(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        plans = Plan.objects.all().order_by('-created')
        plan = plans[0]
        recipeplan = Recipeplan.objects.filter(plan_id=plan.id).order_by('order')
        daynames = Dayname.objects.filter(id__in=recipeplan.values('dayname_id')).order_by('order')
        return render(request, "dashboard.html", {'recipes': recipes, 'plans': plans, 'plan': plan, 'recipeplan': recipeplan, 'daynames': daynames})


class RecipeID(View):
    def get(self, request):
        return render(request, "app-recipe-details.html")


class RecipeList(View):
    def get(self, request):
        return render(request, "app-recipes.html")


class RecipeAdd(View):
    def get(self, request):
        return render(request, "app-add-recipe.html")

    def post(self, request):
        name = request.POST['name']
        description = request.POST["description"]
        preparation = request.POST["preparation"]
        method_of_preparation = request.POST["method_of_preparation"]
        ingredients = request.POST["ingredients"]
        Recipe.objects.create(
            name=name,
            description=description,
            preparation=preparation,
            method_of_preparation=method_of_preparation,
            ingredients=ingredients
        )
        return redirect('/recipe/add/')


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



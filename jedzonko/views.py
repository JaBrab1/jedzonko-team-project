from datetime import datetime
from django.shortcuts import render, redirect, render_to_response
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
import random
from jedzonko.models import Recipe, Plan, RecipePlan, Dayname
from django.db.models import Count
from django.core.paginator import Paginator



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
        recipeplan = RecipePlan.objects.filter(plan_id=plan.id).order_by('order')
        daynames = Dayname.objects.filter(id__in=recipeplan.values('dayname_id')).order_by('order')
        return render(request, "dashboard.html", {'recipes': recipes, 'plans': plans, 'plan': plan, 'recipeplan': recipeplan, 'daynames': daynames})


class RecipeID(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        return render(request, "app-recipe-details.html", {"recipe": recipe})


class RecipeList(View):
    def get(self, request):
        recipe_list = Recipe.objects.all().order_by('-votes', '-created')
        paginator = Paginator(recipe_list, 50)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        return render(request, "app-recipes.html", {'recipes': recipes})


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



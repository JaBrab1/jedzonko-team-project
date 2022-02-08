from django.contrib import admin
from jedzonko.models import Recipe, Plan, Recipeplan, Page, Dayname

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Plan)
admin.site.register(Recipeplan)
admin.site.register(Page)
admin.site.register(Dayname)
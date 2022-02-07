from django.contrib import admin
from jedzonko.models import Recipe, Plan, Dayname, RecipePlan

admin.site.register(Recipe)
admin.site.register(Plan)
admin.site.register(Dayname)
admin.site.register(RecipePlan)

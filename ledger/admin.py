from django.contrib import admin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]


admin.site.register(Recipe, RecipeAdmin)

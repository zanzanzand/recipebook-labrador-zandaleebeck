from django.urls import path

from .views import recipes, recipe

urlpatterns = [
    path('recipes/list', recipes, name='recipes'),
    path('recipe/1', recipe1, name='recipe-1'),
    path('recipe/2', recipe2, name='recipe-2')
]

app_name='ledger'
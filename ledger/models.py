from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])


class Ingredient(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_absoulute_url(self):
        return reverse('ledger:ingredient_detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE,
                                   related_name='recipe')
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='ingredients')

    def __str__(self):
        return f'{self.ingredient.name} - {self.quantity}'
  
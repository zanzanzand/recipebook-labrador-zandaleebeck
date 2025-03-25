from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_add.html"
    form_class = RecipeForm
    success_url = reverse_lazy('ledger:recipes')


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "recipe_add_image.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy(
            "ledger:recipe_detail", kwargs={'pk': self.kwargs['pk']}
        )

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        recipe_image = form.save(commit=False)
        recipe_image.recipe = recipe
        recipe_image.save()
        return redirect('ledger:recipe_detail', pk=recipe.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(
            Recipe, pk=self.kwargs['pk']
        )
        return context


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'

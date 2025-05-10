from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipesList(generic.ListView):
    """View to list all recipes."""
    queryset = Recipe.objects.filter(status='published').order_by('-created_at')
    template_name = 'recipe_list.html'
    # context_object_name = 'recipes'
    # paginate_by = 10  # Number of recipes per page

    # def get_queryset(self):
    #     """Return the list of recipes, ordered by created_at."""
    #     return Recipe.objects.all().order_by('-created_at')
from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipesList(generic.ListView):
    """View to list all recipes."""
    queryset = Recipe.objects.filter(status='published').order_by('-created_at')
    template_name = 'recipes/index.html'  # Template to render the recipe list
    paginate_by = 16  # Number of recipes to display per page

    # def get_queryset(self):
    #     """Return the list of recipes, ordered by created_at."""
    #     return Recipe.objects.all().order_by('-created_at')
from django.shortcuts import render, get_object_or_404
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

def recipe_detail(request, slug):
    """
    View to display a single recipe.

    Context:
    ``recipe``
        An instance of :model `Recipe`.
     **Template:**
    ``recipes/recipe_detail.html``
    """

    queryset = Recipe.objects.filter(status='published')
    recipe = get_object_or_404(queryset, slug=slug)
    return render(
        request, 
        'recipes/recipe_detail.html', 
        {'recipe': recipe}
    )

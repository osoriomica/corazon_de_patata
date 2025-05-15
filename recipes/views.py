from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm

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
    comments = recipe.comments.all().order_by("-created_at")
    comment_count = recipe.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your comment has been submitted and is awaiting approval.",
            )
    comment_form = CommentForm()

    return render(
        request, 
        'recipes/recipe_detail.html', 
        {  
        'recipe': recipe,
         'comments': comments,
         'comment_count': comment_count,
         'comment_form': comment_form,
        }
    )

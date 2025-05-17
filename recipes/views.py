from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from .models import Recipe, Rating, Comment
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
    user_rating = None
    comments = recipe.comments.all().order_by("-created_at")
    comment_count = recipe.comments.filter(approved=True).count()

    # Get the user's rating for the recipe if logged in
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
    
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
         'user_rating': user_rating, 
        }
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status='published')
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.Recipe, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

@login_required
@require_POST
def rate_recipe(request, recipe_id):
    """
    View to handle rating a recipe.
    This view allows users to rate a recipe from 1 to 5 stars.
    If the user has already rated the recipe, it updates the rating.
    If the user is not authenticated, they are redirected to the login page.
    If the rating value is not between 1 and 5, an error message is displayed.
    If the rating is successfully saved, a success message is displayed.
    If the rating is updated, a success message is displayed.
    If the rating is not valid, an error message is displayed.
    Success and error messages are displayed using Django's messages framework.
    This view is decorated with the `@login_required` decorator to ensure that only authenticated users can rate recipes.
    Supports standard form submission and AJAX requests.

    Context:
    ``recipe``
        An instance of :model `Recipe`.
    **Template:**
    ``recipes/recipe_detail.html``
    **Form:**
    ``rating_form``
        A form to submit the rating value.
    **Messages:**
    - Success: "Thank you for your rating!"
    - Error: "Please give a rating value from 1 to 5."
    **Redirects:**
    - Redirects to the recipe detail page after rating.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    rating_value = int(request.POST.get('rating', 0))

    # Validate rating value
    if rating_value < 1 or rating_value > 5:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'error', 
                'message': 'Please give a rating value from 1 to 5.'
            }, status=400)
        
        messages.error(request, "Please give a rating value from 1 to 5.")
        return redirect('recipe_detail', slug=recipe.slug) 
    
    # Check if the user has already rated this recipe
    existing_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
    is_new_rating = existing_rating is None

    if existing_rating:
        # Update the existing rating
        existing_rating.rating = rating_value
        existing_rating.save()
        message = "Your rating has been updated."
    else:
        # Create a new rating
        Rating.objects.create(recipe=recipe, user=request.user, rating=rating_value)
        message = "Thank you for your rating!"
        
    # Calculate the new average rating
    new_average = recipe.average_rating()
    rating_count = recipe.ratings.count()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'average': message,
            'new_average': round(new_average, 1),
            'rating_count': rating_count,
            'is_new_rating': is_new_rating
        })
    
    # Handle non-AJAX request
    messages.success(request, message)
    return redirect('recipe_detail', slug=recipe.slug)
    # Redirect to the recipe detail page with the updated average rating
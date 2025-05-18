from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, JsonResponse
from .models import Recipe, Rating, Comment
from .forms import CommentForm

# Create your views here.


class RecipesList(generic.ListView):
    """
    View to list all recipes.
    Displays a paginated list of recipes with the option to filter by category.

    Context:
    ``recipes``
        A list of :model `Recipe` instances.
    **Template:**
    ``recipes/index.html``
    """
    queryset = Recipe.objects.filter(
        status='published').order_by('-created_at')
    template_name = 'recipes/index.html'  # Template to render the recipe list
    paginate_by = 8  # Number of recipes to display per page


def recipe_detail(request, slug):
    """
    View to display a single recipe.
    Displays a single instance of :model `Recipe` along with its comments
    and ratings.
    It allows users to submit comments and view their own ratings.
    The view handles both GET and POST requests.

    Context:
    ``recipe``
        An instance of :model `Recipe`.
    ``comments``
        A list of comments related to the recipe.
    ``comment_count``
        The number of approved comments for the recipe.
    ``comment_form``
        A form to submit a new comment.
    ``user_rating``
        The user's rating for the recipe, if they are logged in.

     **Template:**
    ``recipes/recipe_detail.html``
    """

    queryset = Recipe.objects.filter(status='published')
    recipe = get_object_or_404(queryset, slug=slug)
    user_rating = None
    comments = recipe.comments.all().order_by("-created_at")
    comment_count = recipe.comments.filter(approved=True).count()

    # Get the user's rating for the recipe if they're logged in
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(recipe=recipe,
                                            user=request.user).first()
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


@login_required
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    Displays a form to edit an existing comment.
    The view handles both GET and POST requests.

    Context:
    ``recipe``
        An instance of :model `Recipe`.
    ``comment``
        An instance of :model `Comment`.
    ``comment_form``
        A form to edit the comment.

    **Template:**
    ``recipes/recipe_detail.html``

    """
    if request.method == "POST":
        queryset = Recipe.objects.filter(status='published')
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    Displays a confirmation page to delete an existing comment.
    The view handles both GET and POST requests.

    Context:
    ``recipe``
        An instance of :model `Recipe`.
    ``comment``
        An instance of :model `Comment`.

    **Template:**
    ``recipes/recipe_detail.html``
    """
    queryset = Recipe.objects.filter(status='published')
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
@require_POST
def rate_recipe(request, recipe_id):
    """
    View to handle rating a recipe.
    It allows users to rate a recipe from 1 to 5 stars.
    Allows users CRUD operations on their own ratings.
    The `@login_required` decorator ensures that only
    authenticated users can rate recipes.
    Supports standard form submission and AJAX requests.

    Context:
    ``recipe``
        An instance of :model `Recipe`.
    ``rating_value``
        The rating value submitted by the user (1 to 5).
    ``existing_rating``
        The existing rating for the recipe by the user, if any.
    ``is_new_rating``
        A boolean indicating whether the rating is new or
        an update to an existing rating.
    ``new_average``
        The new average rating for the recipe after the rating is submitted.
    ``rating_count``
        The total number of ratings for the recipe.

    **Template:**
    ``recipes/recipe_detail.html``

    **AJAX:**
    - Handles AJAX requests to update the rating without a full page reload.

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
    existing_rating = Rating.objects.filter(
        recipe=recipe, user=request.user).first()
    is_new_rating = existing_rating is None

    if existing_rating:
        # Update the existing rating
        existing_rating.rating = rating_value
        existing_rating.save()
        message = "Your rating has been updated."
    else:
        # Create a new rating
        Rating.objects.create(
            recipe=recipe, user=request.user, rating=rating_value)
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

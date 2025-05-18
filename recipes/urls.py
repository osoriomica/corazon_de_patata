from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),
    # URL for the recipe list view
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    # URL for the recipe detail view
    path('recipe/<int:recipe_id>/rate/', views.rate_recipe,
         name='rate_recipe'),
    # URL for rating a recipe
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit,
         name='comment_edit'),
    # URL for editing a comment
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete,
         name='comment_delete')
    # URL for deleting a comment
]

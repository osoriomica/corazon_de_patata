from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),  # URL for the recipe list view
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),  # URL for the recipe detail view
    path('recipe/<int:recipe_id>/rate/', views.rate_recipe, name='rate_recipe'),  # URL for rating a recipe
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),  # URL for the recipe list view
#     path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),  # URL for the recipe detail view
#     path('recipe/add/', views.RecipeCreateView.as_view(), name='recipe_add'),  # URL for adding a new recipe
#     path('recipe/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_edit'),  # URL for editing a recipe
#     path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),  # URL for deleting a recipe
]
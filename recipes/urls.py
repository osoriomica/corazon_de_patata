from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),  # URL for the recipe list view
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),  # URL for the recipe detail view
    # path('bookmarks/', views.BookmarksView.as_view(), name='bookmarks'),
    # path('bookmark/<int:recipe_id>/', views.bookmark_recipe, name='bookmark_recipe'),
    # path('unbookmark/<int:recipe_id>/', views.unbookmark_recipe, name='unbookmark_recipe'),
]
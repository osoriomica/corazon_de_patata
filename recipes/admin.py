from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment, Rating


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Admin view for the Recipe model."""
    summernote_fields = ('description', 'ingredients', 'instructions')
    # Fields to use Summernote editor
    list_display = ('title', 'author', 'created_at', 'status')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'description', 'ingredients', 'instructions')
    prepopulated_fields = {'slug': ('title',)}
    # Automatically populate slug field from title


# Register your models here.
admin.site.register(Comment)
admin.site.register(Rating)


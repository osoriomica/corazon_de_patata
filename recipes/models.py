from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.db.models import Avg

# Create your models here.
class Recipe(models.Model):
    """Model representing a recipe."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    # cloudinary_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    average_rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
        ],
        default='draft'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])
    
class Comment(models.Model):
        """Model representing a comment on a recipe."""
        recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
        user = models.ForeignKey(User, on_delete=models.CASCADE,)
        text = models.TextField()
        approved = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'Comment by {self.user.username} on {self.recipe.title}'
        class Meta:
            ordering = ['-created_at']
    
class Rating(models.Model):
    """Model representing a rating for a recipe."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    def __str__(self):
        return f'{self.user.username} rated {self.recipe.title}: {self.value}'
    class Meta:
        unique_together = ('recipe', 'user')

class Bookmark(models.Model):
    """Model representing a bookmarked recipe by a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    bookmarked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
        ordering = ['-bookmarked_on']
        
    def __str__(self):
        return f'{self.user.username} bookmarked {self.recipe.title}'
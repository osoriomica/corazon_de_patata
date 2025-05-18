# CORAZON DE PATATA
![Responsive Corazon de Patata]()

A recipe-blog dedicated to Indo-Mex recipes for fellow foodies and culinary explorers.

- Homepage listing recipe cards
- Individual recipe pages with details
- User authentication for comments, ratings, and bookmarks
- Recipe filtering/search capabilities
- Admin panel for content management
- Mobile-first design

## Database Schema Planning

1. User Model  

2. Recipe Model  
This will store all recipe information:

- Title | Char(200)
- Slug (Unique) | SlugField
- Author | FK User model
- Image | CloudinaryField, default='placeholder'
- Description | TextField
- Average rating | Calculated field
- Ingredients | TextField
- Instructions | TextField
- Created date | DateTime
- Updated date | DateTime
- Status | Integer

3. Comment Model  
- Recipe | FK Recipe model
- User | FK User
- Comment text | TextField
- Created date | DateTime
- Updated date | DateTime

4. Rating Model  

- Recipe | FK Recipe
- User | FK User
- Rating value (1-5) | IntegerField(validators=[Min(), Max[]])
- Created date | DateTime

5. Bookmark Model  

- User | FK User
- Recipe | FK Recipe
- Created date | DateTime

Custom Error templates tutorial from https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages

Fixtures:
// This file contains a list of recipes with their details.
// Each recipe includes the title, slug, author, description, ingredients, instructions, created_at, updated_at, and status.
// The recipes are categorized into two cuisines: Mexican and Indian.
// The author field references the user who created the recipe.
// The status field indicates whether the recipe is published or not.
// The created_at and updated_at fields are in ISO 8601 format.
// The ingredients and instructions are formatted in HTML lists.
// The recipes are stored in a JSON format suitable for Django fixtures.


VIEWS.PY
Rate_recipe 
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

bugs
Integrity error 
fix: make migratios/migrate to reflect changes

Technologies Used:
Fonts: [fonts.google.com](https://fonts.google.com/)
AI generated images: [Microsoft Copilot](https://copilot.microsoft.com/)
Image converter: [cloudconvert](https://cloudconvert.com/png-to-ico)
Django Allauth Authentication: [allauth](https://docs.allauth.org/en/latest/installation/quickstart.html)
Asynchronous JavaScript And XML to update the user rating without refreshing the entire page: [AJAX](https://developer.mozilla.org/en-US/docs/Glossary/AJAX) 
cloudinary.com
Django 5.2: [Django](https://docs.djangoproject.com/en/5.2/)
Python Virtual Environments: [Python](https://docs.python.org/3/library/venv.html)

References:
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/download/)
- [Django Docs](https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types)


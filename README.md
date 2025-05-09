# corazon_de_patata

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



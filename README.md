# CORAZON DE PATATA
![Corazon de Patata](README-folder/full-screenshots/all-devices-black.png)

![Logo](static/images/logo-lines.png) 

The deployed site can be found here: [Corazon de Patata](https://corazon-de-patata-be3857387485.herokuapp.com/)

<strong>Click here to view full screenshots of the website.

[Full Screenshots](README-folder/full-screenshots)  </strong>


---

## 📑 Table of Contents

- [Introduction](#introduction)
- [UXD](#uxd)
  - [User Stories](#user-stories)
  - [Features](#features)
  - [Design](#design)
- [Database Schema](#database-schema)
- [Fixtures](#fixtures)
- [Views](#views)
- [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Validation](#validation)
  - [Manual Testing](#manual-testing)
  - [Fixed Bugs](#fixed-bugs)
- [Deployment](#deployment)
- [Running the Project Locally](#running-the-project-locally)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

---

## 🧑‍🍳 Introduction

**CORAZON DE PATATA** is a Django-powered food blog inspired by Indo-Mexican fusion cuisine. It allows users to discover, rate, comment on, and bookmark recipes. The site includes full backend functionality with admin controls, user authentication, and AJAX-powered interactions.

---

## UXD

### User Stories

- As a user, I want to browse recipes easily.
- As a user, I want to view full recipe details including ingredients and instructions.
- As a user, I want to log in and leave comments or rate recipes.
- As a user, I want to save recipes I like to my bookmarks. * Future deployment
- As an admin, I want to manage submitted content efficiently.

### Features

- 🔍 **Homepage**: Recipe card previews with filters and search  
- 📝 **Recipe Detail Pages**: Ratings, comments, and full instructions  
- ✅ **Authentication**: Django Allauth-powered login/signup/logout  
- ⭐ **Ratings**: 1–5 star rating system with AJAX updates  
- 📘 **Bookmarks**: Save your favorite dishes  * Future deployment
- 🛠️ **Admin panel**: Manage users, content, and moderation  
- 📱 **Responsive Design**: Optimized for all screen sizes  

### Design
The color scheme and fonts reflect the warmth and spice of the Indo-Mexican kitchen. Typography is chosen to balance elegance with readability. All layouts are designed with mobile-first principles.
- Colour Palette:

    | Color                                                                 | Hex       | Name         |
    |----------------------------------------------------------------------|-----------|--------------|
    | ![#CE4F19](https://placehold.co/15x15/CE4F19/CE4F19.png)             | #CE4F19   | Red-orange   |
    | ![#D5820C](https://placehold.co/15x15/D5820C/D5820C.png)             | #D5820C   | Orange       |
    | ![#03823A](https://placehold.co/15x15/03823A/03823A.png)             | #03823A   | Green        |
    | ![#333333](https://placehold.co/15x15/333333/333333.png)             | #333333   | Dark Gray    |
    | ![#f8da9e](https://placehold.co/15x15/f8da9e/f8da9e.png)             | #f8da9e   | Light Beige  |
    | ![#feb495](https://placehold.co/15x15/feb495/feb495.png)             | #feb495   | Peach        |

- Typography:
    The font families were chosen to balance playfulness with readability.
    - Lato for the body and general text elements.
    - Fredericka the Great for the headings and highlighted text.


---

## 📊 Database Schema
### User Model  
Standard Django `User` model extended with Allauth.

### Recipe Model  
Includes:
- `title`, `slug`, `author`, `image`, `description`
- `ingredients`, `instructions`, `average_rating`
- `created_on`, `updated_on`, `status`

### Comment Model  
- FK to `Recipe` and `User`, plus `body`, `created_on`, `updated_on`

### Rating Model  
- FK to `Recipe` and `User`, `value` (1–5), `created_on`

### Bookmark Model  
- FK to `Recipe` and `User`, `created_on`

---

## 📦 Fixtures
Fixture files are included in JSON format and contain:
- Pre-filled recipes in Mexican and Indian categories  
- All relevant fields including HTML-formatted content  

---

## 🔍 Views
### `rate_recipe` view

Handles:
- Auth-check
- Duplicate detection and update
- Valid range enforcement
- Message feedback via Django’s messages framework
- AJAX and standard form submission

---

## 🧰 Wireframes
ireframes and mockups created with [Canva](https://www.canva.com/) and [Website Mockup Generator](https://websitemockupgenerator.com/).

<details>
<summary>Click to view wireframes</summary>

**Mobile**  
![Mobile wireframe](README-folder/wireframes/mobile-wireframe.jpg)

**Desktop**  
![Desktop wireframe](README-folder/wireframes/desktop-wireframe.jpg)
</details>

---

## 💻 Technologies Used

- [Django 5.2](https://docs.djangoproject.com/en/5.2/)
- [Heroku](https://www.heroku.com/)
- [Cloudinary](https://cloudinary.com/)
- [Django Allauth](https://docs.allauth.org/en/latest/)
- [Bootstrap 5.3](https://getbootstrap.com/)
- [AJAX](https://developer.mozilla.org/en-US/docs/Glossary/AJAX)
- [Google Fonts](https://fonts.google.com/)
- [cloudconvert](https://cloudconvert.com/)
- [PE8CI](https://pep8ci.herokuapp.com/#)
- [Mockup Generator](https://websitemockupgenerator.com/)

---

## 🧪 Testing

### Validation

[Validation Folder](README-folder/validation)
- HTML/CSS/JS validated using [W3C Validator](https://validator.w3.org/) and [JSHint](https://jshint.com/)

- Python code checked with [PE8CI](https://pep8ci.herokuapp.com/#)

### Manual Testing
<strong>Manual testing</strong> involves checking a project’s functionality by simulating user interactions, typically through clicking buttons, filling out forms, and testing the logic and responsiveness in different browsers and resolutions. It is an essential way to ensure that a product meets the user's expectations but comes with limitations. It can be time-consuming, resource-intensive, and prone to human error,  making it unreliable (especially for larger projects). Tiredness, biases, and/or oversight can lead to missed bugs and issues that can dampen the user’s experience. Manual testing is best deployed when we need to assess the user experience (UX), or when testing specific user stories that require human judgment to evaluate nuances, which would not be picked by automated tests. 

<strong>Automated testing</strong>, on the other hand, uses code to run tests on software, providing a faster, scalable solution for detecting errors early in the development process. Automated tests can be written to target specific scenarios and run hundreds of tests in a short amount of time, making them ideal when verifying that new code hasn't broken existing functionality. However, automated tests are only as reliable as the test cases designed to check, and they do not assess the user experience. Therefore, a combination of manual and automated testing is often the best approach, where automated testing handles repetitive tasks and error detection; manual testing focuses on areas where human insight and user experience are critical. 

This site was thoroughly tested using a <strong>manual testing</strong> approach. These tests led to catching and fixing issues from early in the development. Some friends and family also contributed towards testing the game’s logic and provided valuable feedback. 

Please see below for the tests and final results:

Tested across:
- Chrome, Firefox, Safari (desktop & mobile)
- All core views tested with both authenticated and guest users

| Feature          | Test Scenario                           | Result |
|------------------|------------------------------------------|--------|
| Login Required   | Rating/commenting                        | Pass   |
| Valid/Invalid Rating | Rating value out of range check     | Pass   |
| Mobile UI        | Screen sizes < 768px                     | Pass   |
| Admin Panel      | CRUD operations                          | Pass   |
| Ratings           | Ratings persist across user sessions    | Pass   |
| Form validation | Comments and ratings are sent successfully | Pass |
| Message handling | Messages are displayed to the user on Post | Pass |

### Fixed Bugs

- **IntegrityError** during DB updates  
  Fix: `makemigrations` and `migrate` rerun after model adjustments  
- **Rating update** was duplicating entries  
  Fix: `get_or_create()` + `update()` logic in view  
- **AJAX errors** on unauthenticated users  
  Fix: Client-side check for auth before submitting via JS  
- **404 not styled**  
  Fix: Custom templates following [LearnDjango's tutorial](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)

---

## 🚀 Deployment
<strong>Create a GitHub Repository</strong>  
	1. Go to [GitHub website](https://github.com/) and navigate to the <strong>Settings</strong> tab.  
	2. [Create a new public repository](https://github.com/new) using the format username.github.io, where username is your GitHub username.    
	3. Optionally, add a repository description, select whether it will be public or private, and initialise it with a README file (optional).  
	4. <strong>Forking:</strong> If deploying a project you don’t own, fork the repository first by clicking the "Fork" button at the top right of the project repository.  
	5. Configure GitHub Pages later in the settings.  
2. <strong>Clone and Deploy a Project</strong>  
	1. (Optional) Install [GitHub Desktop](https://desktop.github.com/) if you prefer a graphical interface for managing repositories.  
	2. Clone the repository:  
		* After installing GitHub Desktop (if you're using it), refresh the page on GitHub and click the “Set up in Desktop” button.  
		* The GitHub Desktop app will open. Select a location to save the project and clone it.  
	3. Create an <strong>index.html</strong> file for your project if it doesn’t already exist.  
	4. Use the terminal to:  
		* <strong>Add</strong> your changes: git add .  
		* <strong>Commit</strong> your changes: git commit -m "Initial commit"  
		* <strong>Push</strong> your changes: git push origin main  
3. <strong>Clone and Deploy This Project</strong>  
	1. Go to my GitHub repository for this project: [Corazon de Patata](https://github.com/osoriomica/corazon_de_patata).  
	2. In the top right corner of the repository page, click the green Gitpod icon to open a new workspace in Gitpod.
	3. You can choose to work locally or download the project and edit it in an IDE like [Visual Studio Code](https://code.visualstudio.com/download).

### Deploy to [Heroku](https://www.heroku.com/) using the following steps:

1. Create `Procfile`, `requirements.txt`, `runtime.txt`
2. Set allowed hosts and static file settings in `settings.py`
3. Set up Cloudinary and environment variables
4. Push to GitHub → connect to Heroku via GitHub integration
5. Enable automatic deploys and run `heroku run python manage.py migrate`

---

## 🛠️ Running the Project Locally  

To run this project locally, follow the steps below:  

### 1. Clone the repository  
>```bash  
>git clone https://github.com/yourusername/corazon-de-patata.git  
>cd corazon-de-patata  
### 2. Create and activate a virtual environment  
>python3 -m venv venv  
>source venv/bin/activate  # On Windows: venv\Scripts\activate  
### 3. Install project dependencies  
>pip install -r requirements.txt  
### 4. Set environment variables  
Create a .env file in the root directory and include:  
>SECRET_KEY=your-django-secret-key  
>DEBUG=True  
>DATABASE_URL=sqlite:///db.sqlite3  
>CLOUDINARY_URL=your-cloudinary-url  
>ALLOWED_HOSTS=127.0.0.1,localhost  
### 5. Apply migrations and load fixtures  
>python manage.py migrate  
>python manage.py loaddata recipes.json  
### 6. Run the development server  
>python manage.py runserver    
Visit http://127.0.0.1:8000 in your browser.  

---

## Credits

### Code

- [DjangoDocs](https://docs.djangoproject.com/)
- Custom error handling via [LearnDjango](https://learndjango.com/)
- Rating form adapted from various StackOverflow examples
- [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) for general reference in layout styling, navigation bars and modals, etc.

### Media

- AI-generated food images and site's logo from [MicrosoftCopilot](https://copilot.microsoft.com/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Fonts from [GoogleFonts](https://fonts.google.com/)
- Converted via [cloudconvert](https://cloudconvert.com/png-to-ico)

### Acknowledgements

Thanks to my mentor and the Django community for consistent support and detailed documentation. Also, a big thanks to the developers of Allauth, Cloudinary, and all open-source tools that power this project.

---

🍲 *Cook with love. Code with spice.*
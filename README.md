
# Jedzonko — Meal Planning Web Application

**Team Project | Coders Lab Python Developer Course | 2022**

## About the Project

Jedzonko is a web application developed using Python and Django as part of a team project during the Coders Lab Python Developer course.

The application allows users to manage cooking recipes, create meal plans, and organize meals into schedules.

The project was developed in a Scrum-based workflow, using Git, feature branches, pull requests, and collaborative code integration.

This repository preserves the original development history from 2022.

## Features

The application includes:

- Browsing recipes and viewing recipe details
- Adding, editing, and deleting recipes
- Creating and managing meal plans
- Assigning recipes to meal schedules
- Displaying meal plans on a dashboard
- Recipe voting and paginated recipe listings
- Basic user account and authentication functionality

These features represent the combined work of the development team.

## Technologies

**Backend**
- Python
- Django 2.2.6
- Django ORM

**Database**
- PostgreSQL
- SQL

**Frontend**
- HTML
- CSS
- JavaScript
- Django Templates

**Development and Collaboration**
- Git
- GitHub
- Scrum
- Feature branches
- Pull requests

## My Contributions

**Bartosz — GitHub: JaBrab1 / BartoszIkwanty**

My responsibilities focused primarily on Django backend development and integration with the application's frontend templates.

Based on the original Git commit history, my contributions included:

- Implementing Django views and URL routing
- Developing dashboard-related functionality
- Working on the `Plan` data model and database migrations
- Retrieving and filtering data using Django ORM
- Implementing meal plan detail views
- Developing recipe editing functionality, including handling form submissions and updating database records
- Integrating backend functionality with HTML templates
- Participating in code integration and collaborative development

### Selected Commits

The following commits document examples of my work:

- [3a115cd](../../commit/3a115cd) — Initial dashboard implementation
- [64212b3](../../commit/64212b3) — Django views and URL routing
- [f5ac606](../../commit/f5ac606) — Dashboard data integration
- [20f0024](../../commit/20f0024) — Meal plan model and related changes
- [53dc4bb](../../commit/53dc4bb) — Recipe editing functionality
- [5430bc1](../../commit/5430bc1) — Recipe editing improvements

The project was developed collaboratively. The contributions listed above reflect my documented work rather than ownership of the entire application.

## Project Structure

```text
Jedzonko/
├── jedzonko/           # Django application
│   ├── models.py       # Database models
│   ├── views.py        # Application views
│   └── migrations/     # Database migrations
├── scrumlab/           # Django project configuration
├── static/             # CSS, JavaScript and static assets
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Installation and Setup

This is a legacy educational project from 2022. It uses older versions of Python/Django dependencies and has not been verified in a modern environment.

### 1. Clone the repository

```bash
git clone https://github.com/JaBrab1/jedzonko-team-project.git
cd jedzonko-team-project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment:

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

The application expects database settings in `scrumlab/local_settings.py`.

Create this file and configure your local PostgreSQL connection:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "jedzonko",
        "USER": "your_local_db_user",
        "PASSWORD": "your_local_db_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

Additional configuration or sample records may be necessary. These instructions have not been verified against current dependency versions.

## Team Collaboration

The application was created as a collaborative project during the Coders Lab Python Developer course in 2022.

Development followed a Scrum-style workflow, including task distribution, feature branches, pull requests, and code integration.

The original Git history has been preserved to document the development process and contributions of the team members.

## Credits

- **Coders Lab** — Course materials and initial project resources
- **Project team** — Collaborative application development

[Original team repository](https://github.com/CodersLab/WAR_SPY_S_294_ScrumLab)

[Original course instructions](CODERSLAB_INSTRUCTIONS.md)

[View commit history](../../commits/main)

## Project Status

**Archived educational project — 2022**

This repository is maintained as part of my programming portfolio to demonstrate my early experience with Django, database operations, backend development, and teamwork.

The application is not production-ready and would require dependency updates, configuration improvements, and a security review before deployment.

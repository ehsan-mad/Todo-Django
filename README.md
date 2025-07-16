
# Django To-Do Application

A feature-rich To-Do application built with Django that allows users to manage their tasks with user authentication, task categorization, and status tracking.

## Features

- User Authentication (Login/Register)
- Task Management (Create, Read, Update, Delete)
- Task Categories (General, Work, Others)
- Task Status Tracking (Pending, Completed)
- Due Date and Time Management
- Responsive Bootstrap UI with Crispy Forms
- User-specific task management

## Tech Stack

- **Backend:** Django 5.2.3
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap 5
- **Forms:** Django Crispy Forms with Bootstrap 5
- **Authentication:** Django Built-in Authentication

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- MySQL server
- pip (Python package installer)
- Virtual environment (recommended)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ehsan-mad/Todo-Django.git
cd Todo-Django
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django==5.2.3
pip install mysqlclient
pip install django-crispy-forms
pip install crispy-bootstrap5
```

Or create a `requirements.txt` file:

```txt
Django==5.2.3
mysqlclient==2.2.4
django-crispy-forms==2.0
crispy-bootstrap5==0.7
```

Then install:
```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### MySQL Database Configuration

1. **Create MySQL Database:**
   ```sql
   CREATE DATABASE task_db;
   ```

2. **Update Database Settings:**
   Edit `Task/settings.py` and update the database configuration:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'task_db',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306'
       }
   }
   ```

3. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

   ```
**The database of the project is main directory you can export the db in the mysql for the setup**

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`



### Production Deployment Steps

#### 1. Environment Configuration

1. **Update Settings for Production:**
   ```python
   # In Task/settings.py
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   
   # Add static files configuration
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATIC_URL = '/static/'
   
   # Security settings
   SECURE_SSL_REDIRECT = True
   SECURE_HSTS_SECONDS = 31536000
   SECURE_HSTS_INCLUDE_SUBDOMAINS = True
   SECURE_HSTS_PRELOAD = True
   ```

2. **Environment Variables:**
   Create a `.env` file for sensitive information:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   DATABASE_URL=mysql://username:password@localhost/task_db
   ```

#### 2. Database Migration

```bash
python manage.py collectstatic --noinput
python manage.py migrate
```



## API Endpoints

- `/` - Task list (home page)
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout
- `/task/create/` - Create new task
- `/task/update/<id>/` - Update existing task
- `/task/delete/<id>/` - Delete task
- `/admin/` - Django admin panel

### Development Tips

- Use `python manage.py runserver` for development

## Screenshots or screencast showing app functionality

[View Screenshots and Demo](https://drive.google.com/drive/folders/1wDGavxbHgwHWSf0_KGvfq1CZghNUJElr?usp=sharing)

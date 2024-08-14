# Project Management System

This is a simple project management system built with Django. It allows you to create, view, edit, and delete projects and tasks.

## Features

- List all projects
- View details of a project and its associated tasks
- Create new projects and tasks
- Edit existing projects and tasks
- Delete projects and tasks

## Requirements

- Python 3.x
- Django

## Setup Instructions

1. Clone this repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate into the project directory:
    ```bash
    cd project_management_system
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser for the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:
    ```bash
    python manage.py runserver
    ```

9. Access the application in your browser:
    - Project list: `http://127.0.0.1:8000/`
    - Admin panel: `http://127.0.0.1:8000/admin/`

## Notes

- This project uses SQLite as the default database.
- No static files (CSS/JS) are used, only inline styles for simplicity.


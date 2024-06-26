# Heart Monitor Project

This is a Django-based project to monitor heart rates and manage patients. It includes user registration and login, patient management, and heart rate recording functionalities.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Assumptions and Decisions](#assumptions-and-decisions)
- [API Documentation](#api-documentation)
- [Additional Information](#additional-information)

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git (optional, for version control)

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/asifahmad01/heartmoniter.git
    cd heartmoniter
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin user.

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    The project should now be running at `http://127.0.0.1:8000/`.

## Running the Project

Project Structure

heartmoniter/
├── home/
│   ├── migrations/
│   ├── templates/
│   │   └── home/
│   │       ├── register.html
│   │       ├── login.html
│   │       └── admin.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── heartmonitor/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md





To start the development server, navigate to your project directory and run:

```bash
source env/bin/activate  # Activate the virtual environment
python manage.py runserver

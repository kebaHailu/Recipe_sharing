# Custom Authentication API
Recipe Sharing 
This project provides a custom authentication API using Django and Django REST Framework (DRF). It includes a custom token obtain pair serializer for user authentication.

## Features

- Custom user authentication with email and password.
- Token-based authentication using JWT (JSON Web Tokens).
- Custom error messages for authentication failures.
- has 3 Django apps include comment, recipe and Recipe sharing

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kebaHailu/recipe_sharing.git
    cd yourproject
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Endpoints and  Authentication 
- `/user/create` - for create a new user by using his first_name, last_name, email and password
- `/user/token` - for login using email and password 
- `/recipe/` - for list of recipes and also create a recipe for verifed user only 
- `/comment/` - for list of comments and also create a comment for verifed user only 

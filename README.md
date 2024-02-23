# trees-everywhere
Trees Everywhere is a project to connect volutaries around the world to plant new trees.

## Stack in use:
- Python - version 3.9
- Django Framework - version 4.2
- poetry - version 1.7.1
- pre-commit - version 3.6.2
    - black - 24.2.0
    - isort -5.13.2
- Django Rest Framework - version 3.14.0

## Tasks developed:

- Create admin pages for:
    - Create new users and passwords, allowing connect a user to an account;
    - List and create accounts, allowing activate and deactivate from the account list screen;
    - Create and read trees, showing all the trees with the name who planted;
- Create template view to a user login;
- Create API REST method to return all the trees planted by logged user.

## Instructions to run

1. Install Python:
    - On Windows: `pip install python3.9`
    - On distro Linux: `sudo apt-get install python3.9`

2. Install poetry:
    - On Windows: `(Invoke-WebRequest -Uri https://install.python-poetry.org | Invoke-Expression)`
    - On distro Linux: `curl -sSL https://install.python-poetry.org | python3 -`
    - Or `pip install poetry==1.7.1`

3. Install the dependencies:
    - `poetry install`

4. Activate the virutal environment:
    - `poetry shell`

5. Run the migrations:
    - `python manage.py migrate`

6. Run the development server:
    - `python manage.py runserver`

7. Now you can see the project at `http://localhost:8000/`!


## Mapping
- Templates paths
    - `admin/` -> to enter the admin platform
    - `login/` -> to regular users login the website
    - `index/` -> page that is redirected after login
- API routes
    - `api/planted_tree/` -> to show all trees planted by the logged user

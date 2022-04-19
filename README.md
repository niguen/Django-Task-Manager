# Django-Task-Manager

A simple task manager created with Django and Bootstrap.

![Main View](/docs/Task_manager_1.PNG "Main View")

![Add Task View](/docs/Task_manager_2.PNG "Add Task View")


## Installation

1. After cloning the project navigate to the project directory and install the required python libraries listed in requirements.txt.

    `pip install reuirements.txt`

2. Next, create the the database by running the followinig commands:

    `python manage.py makemigrations`

    `python manage.py migrate`

3. Create an administrator user account:

    `python manage.py createuser admin`

4. Start the server:

    `python manage.py runserver`

## Add a user

Users can only be added by the Administrator and through the [Admin pannel](127.0.0.1:8000/admin).


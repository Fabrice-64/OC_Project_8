# Overall Framework
This project is developped in the framework of an education program as software developper in Python.

# Purpose
This web application offers the user to look for food items with better nutritional properties.

# Main Functionalities
- The user can create an account in order to get a better experience
- The user, be he anonymous or registered, is supposed to type in the name of a food item
- Then, the application looks for items of the same category with better nutritional properties
- The user can get more information on a selected product
- And he can subsequently record it

# Environment
This project is developped using Python 3.8.1 and Django 3.1.2

# Script for efficient testing:
Using the Shell, type what the following command line, it will remove almost all irrelevant files.

$ coverage run --omit='*/venv/*,*/tests/*,*/migrations/*,*/papounet_diet/tests.py,*/papounet_diet/settings.py,*/manage.py,*/apps.py,*/admin.py'  manage.py test
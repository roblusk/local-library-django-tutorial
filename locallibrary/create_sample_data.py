import os
import django
from faker import Faker
import random

# Configure settings for project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

# Load the Django project's settings
django.setup()

# Import modules
from catalog.models import Genre, Book, BookInstance, Author, Language

# Initialize Faker instance
fake = Faker()
Faker.seed(1) # generate consistent sample data


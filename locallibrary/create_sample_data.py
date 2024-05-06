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
random.seed(1)

# Create 6 Genres
for _ in range(6):
    genre_name = fake.word()
    genre, _ = Genre.objects.get_or_create(name=genre_name)
    genre.save()
print(f"There are now {Genre.objects.count()} genres in the database.")

# Create 6 languages
for _ in range(6):
    language_name = fake.language_name()
    language, _ = Language.objects.get_or_create(name=language_name)
    language.save()
print(f"There are now {Language.objects.count()} languages in the database.")

# Create 10 authors
from datetime import date
for _ in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=100)
    author, _ = Author.objects.get_or_create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
    author.save()
print(f"There are now {Author.objects.count()} authors in the database.")

# Create 50 books
authors = Author.objects.all()
genres = Genre.objects.all()
languages = Language.objects.all()
for _ in range(50):
    title = fake.sentence(nb_words=5)
    author = random.choice(authors)
    summary = fake.text()
    isbn = fake.isbn13()
    language = random.choice(languages)
    
    if Book.objects.filter(isbn=isbn).exists():
        continue

    book, _ = Book.objects.get_or_create(title=title, author=author, summary=summary, isbn=isbn, language=language)
    for _ in range(random.randint(1, 3)):
        book.genre.add(random.choice(genres))
    
    book.save()
print(f"There are now {Book.objects.count()} books in the database.")

books = Book.objects.all()
# Create 250 book instances
for _ in range(250):
    book = random.choice(books)
    imprint = fake.unique.random_number(digits=5)
    due_back = random.choice(
        [None,
        fake.date_time_this_year(before_now=False, after_now=True)
        ])
    book_instance = BookInstance(book=book, imprint=imprint, due_back=due_back)
    book_instance.save()
print(f"There are now {BookInstance.objects.count()} book instances in the database.")

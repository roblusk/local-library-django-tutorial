from django.db import models

# Create your models here.

# Genere model
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, unique=True, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            )
        ]
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            )
        ]
    
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('language-detail', args = [str(self.id)])

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book"
        )
    isbn = models.CharField(
        'ISBN',
        max_length = 13,
        unique =True,
        help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn''">ISBN number</a>'
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Select a language for this book"
        )

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'
    
import uuid

class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library"
        )
    book = models.ForeignKey('Book', on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availablity'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args = [str(self.id)])
    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'
    def full_name(self):
        return self.first_name + " " + self.last_name



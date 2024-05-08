from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Bookfields = ["title", "author", "summary", "isbn", "genre", "language"]
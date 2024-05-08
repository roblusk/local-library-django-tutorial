from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_meep_books = BookInstance.objects.filter(book__title__icontains="meep").count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_meep_books': num_meep_books,
    }

    return render(request, 'index.html', context=context)

# def books_list(request):
#     available_books = Book.objects.filter(bookinstance__status__exact='a').distinct()
#     context = {
#         'available_books': available_books
#     }
#     return render(request, 'books_list.html', context=context)

from django.views import generic
class BookListView(generic.ListView):
    model=Book

class BookDetailView(generic.DetailView):
    model = Book
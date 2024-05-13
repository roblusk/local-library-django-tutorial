from django.shortcuts import render, redirect
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required
from .forms import BookForm

@login_required
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
    paginate_by = 10
    template_name = "../../templates/catalog/book_list.html"
class BookDetailView(generic.DetailView):
    model = Book

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("book-detail", pk=book.pk)
    else:
        form = BookForm()
    
    context = {"form": form}

    return render(request, "catalog/book_form.html", context=context)

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("book-detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    
    context = {"form": form}

    return render(request, "catalog/book_form.html", context=context)


from django.contrib.auth.mixins import LoginRequiredMixin
class AuthorListView(LoginRequiredMixin, generic.ListView):
    model=Author
    paginate_by = 10
class AuthorDetailView(generic.DetailView):
    model=Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
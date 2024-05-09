from django.urls import path
from . import views

from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name='index'),
    #path('books/', views.books_list, name='books'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/create/', views.book_create, name="book-create"),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path('grid/', TemplateView.as_view(template_name="grid.html"), name="bootstrap")
]
from django.contrib import admin

# Register your models here.
from .models import Genre, Language, Book, BookInstance, Author

admin.site.register(Genre)
admin.site.register(Language)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availablity', {
            'fields': ('status', 'due_back')
        })
    )

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    fields = ['first_name', 'last_name', 'date_of_birth']
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)
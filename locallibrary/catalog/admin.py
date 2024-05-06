from django.contrib import admin

# Register your models here.
from .models import Genre, Language, Book, BookInstance, Author

admin.site.register(Genre)
admin.site.register(Language)

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
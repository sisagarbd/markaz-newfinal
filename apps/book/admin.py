from django.contrib import admin
from .models import Book, Author, Catagory, LibraryBranch, Publisher, Tag
# Register your models here.

class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug')
    search_fields = ('tag_name',)
    ordering = ('tag_name',)


class LibraryBranchAdmin(admin.ModelAdmin):
    list_display = ('Library_name', 'location', 'city')
    search_fields = ('Library_name', 'location', 'city')
    ordering = ('Library_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catagory_name', 'slug')
    search_fields = ('catagory_name',)
    ordering = ('catagory_name',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('Publisher_name',)
    search_fields = ('Publisher_name',)
    ordering = ('Publisher_name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'date_of_birth', 'date_of_death')
    search_fields = ('author_name',)
    ordering = ('author_name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('B_title',)
    list_filter = ( 'B_title',)
    search_fields = ('B_title',)
    ordering = ('B_title',)
    list_per_page = 10

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Catagory, CategoryAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(LibraryBranch, LibraryBranchAdmin)

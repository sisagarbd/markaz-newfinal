from django.urls import path
from apps.book.book_list.views import BookListView
from apps.book.book_add.views import BookAddView
from django.contrib.auth.decorators import login_required
from apps.book.book_update.views import BookUpdateView
from apps.book.book_delete.views import BookDeleteView
from apps.book.Catagory_view.views import BookCatagoryView, BookAuthorView, BookLibraryView, BookPublisherView

urlpatterns = [
    path(
        "list/",
        login_required(BookListView.as_view(template_name="book_list.html")),name="book_list",
    ),
    path(
        "add/",
        login_required(BookAddView.as_view(template_name="book_add.html")),name="book_add",
    ),
    path(
        "update/<int:pk>/",
        login_required(BookUpdateView.as_view(template_name="book_update.html")), name="book_update",

    ),
    path(
        "delete/<int:pk>/",
        login_required(BookDeleteView.as_view()), name="book_delete",
    ),
    path(
        "ajax/add_author/",
        BookAddView.ajax_add_author, name="ajax_add_author",
    ),
    path(
        "book_detail/",
        login_required(BookListView.as_view(template_name="book_details.html")), name="book_detail",
    ),
    path(
        "book_catagory/",
        login_required(BookCatagoryView.as_view(template_name="catagory/book_catagory.html")), name="book_catagory",
    ),
    path(
        "book_author/",
        login_required(BookAuthorView.as_view(template_name="author/book_author.html")), name="book_author",
    ),
    path(
        "library/",
        login_required(BookLibraryView.as_view(template_name="library/book_library.html")), name="book_library",
    ),
    path(
        "publisher/",
        login_required(BookPublisherView.as_view(template_name="publisher/book_publisher.html")), name="book_publisher",
    ),

]

from django.urls import path
from apps.book.book_list.views import BookListView
from apps.book.book_add.views import BookAddView
from django.contrib.auth.decorators import login_required
from apps.book.book_update.views import BookUpdateView
from apps.book.book_delete.views import BookDeleteView
from apps.book.Catagory_view.views import BookCatagoryView, BookCatagoryAdd, CatagoryDeleteView, CatagoryEditView
from apps.book.Author_view.views import BookAuthorView, BookAuthorAdd, AuthorDeleteView, AuthorEditView
from apps.book.Library_view.views import BookLibraryView, BookLibraryAdd, LibraryDeleteView, LibraryEditView
from apps.book.Publisher_view.views import BookPublisherView, BookPublisherAdd, PublisherDeleteView, PublisherEditView

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
        "book_catagory/add",
        login_required(BookCatagoryAdd.as_view(template_name="catagory/book_catagory_add.html")), name="book_catagory_add",
    ),

    path(
        "book_catagory/delete/<int:pk>/",
        login_required(CatagoryDeleteView.as_view()), name="book_catagory_delete",
    ),
     path(
        "book_catagory/edit/<int:pk>/",
        login_required(CatagoryEditView.as_view(template_name="catagory/book_catagory_edit.html")), name="book_catagory_edit",
    ),

    path(
        "book_author/",
        login_required(BookAuthorView.as_view(template_name="author/book_author.html")), name="book_author",
    ),

     path(
        "book_author/add",
        login_required(BookAuthorAdd.as_view(template_name="author/book_author_add.html")), name="book_author_add",
    ),
    path(
        "book_author/delete/<int:pk>/",
        login_required(AuthorDeleteView.as_view()), name="book_author_delete",
    ),

    path(
        "book_author/edit/<int:pk>/",
        login_required(AuthorEditView.as_view(template_name="author/book_author_edit.html")), name="book_author_edit",
    ),

    path(
        "library/",
        login_required(BookLibraryView.as_view(template_name="library/book_library.html")), name="book_library",
    ),

    path(
        "library/add",
        login_required(BookLibraryAdd.as_view(template_name="library/book_library_add.html")), name="book_library_add",
    ),

    path(
        "library/delete/<int:pk>/",
        login_required(LibraryDeleteView.as_view()), name="book_library_delete",
    ),
    path(
        "library/edit/<int:pk>/",
        login_required(LibraryEditView.as_view(template_name="library/book_library_edit.html")), name="book_library_edit",
    ),

    path(
        "publisher/",
        login_required(BookPublisherView.as_view(template_name="publisher/book_publisher.html")), name="book_publisher",
    ),

    path(
        "publisher/add",
        login_required(BookPublisherAdd.as_view(template_name="publisher/book_publisher_add.html")), name="book_publisher_add",
    ),

    path(
        "publisher/delete/<int:pk>/",
        login_required(PublisherDeleteView.as_view()), name="book_publisher_delete",
    ),
     path(
        "publisher/edit/<int:pk>/",
        login_required(PublisherEditView.as_view(template_name="publisher/book_publisher_edit.html")), name="book_publisher_edit",
    ),


]

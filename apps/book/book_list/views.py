from django.views.generic import TemplateView
from web_project import TemplateLayout
from apps.book.models import Book

class BookListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        books = self.get_annoteted_books()

        context.update(
            {
                "books": books,
                "books_count": Book.objects.count(),
            }
        )
        return context


    def get_annoteted_books(self):
        return Book.objects.all().order_by('id')

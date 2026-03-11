from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.book.forms import BookForm
from django.db.models import Q
from apps.book.models import Book
from django.shortcuts import redirect
from django.contrib import messages


class BookUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['book_id'] = self.get_book(self.kwargs['pk'])
        return context

    def post(self, request, pk):
        book = self.get_book(pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            if not self.book_exitsts(form.cleaned_data, book):
                form.save()
                messages.success(request, 'Book Updated')
            else:
                messages.error(request, 'Book Already Exists')
        else:
            messages.error(request, 'Book Update Failed')
        return redirect('book_list')


    def get_book(self, pk):
        return Book.objects.get(pk=pk)

    def book_exitsts(self, cleaned_data, current_book):
         matching_books = Book.objects.filter(
             Q(customer__iexact=cleaned_data['customer']) &
             Q(transaction_date=cleaned_data['transaction_date']) &
             Q(due_date=cleaned_data['due_date']) &
             Q(total=cleaned_data['total']) &
             Q(status=cleaned_data['status'])
         ).exclude(pk=current_book.pk)
         return matching_books.exists()

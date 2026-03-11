from django.views.generic import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from apps.book.models import Book
from django.contrib import messages

class BookDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ("transactions.delete_transaction")

    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()
        messages.success(request, 'Book Deleted')
        return redirect('book_list')

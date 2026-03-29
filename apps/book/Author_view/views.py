from django.views.generic import TemplateView, DeleteView
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.book.models import Catagory, Author
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

#WORKING
class BookAuthorView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))


        context.update(
            {
                "Authors": Author.objects.all().order_by('id'),
            }
        )

        return context




class BookAuthorAdd(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            author_name = request.POST.get("authorName")
            date_of_birth = request.POST.get("date_of_birth")
            date_of_death = request.POST.get("date_of_death")



            Author.objects.create(
                author_name=author_name, date_of_birth=date_of_birth, date_of_death=date_of_death
            )

            # Catagory.objects.create(catagory_name=catagory_name, slug= slug)
            return redirect('book_author')




class AuthorDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ("transactions.delete_transaction")

    def get(self, request, pk):
        author = get_object_or_404(Author, id=pk)
        author.delete()
        messages.success(request, 'Author Deleted')
        return redirect('book_author')









class AuthorEditView(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.delete_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        author = get_object_or_404(Author, id=self.kwargs['pk'])
        context['author'] = author

        return context

    def post(self, request, *args, **kwargs):
        author = get_object_or_404(Author, id=self.kwargs['pk'])

        author_name = request.POST.get("authorName")
        date_of_birth = request.POST.get("date_of_birth")
        date_of_death = request.POST.get("date_of_death")

        author.author_name = author_name
        author.date_of_birth = date_of_birth
        author.date_of_death = date_of_death
        author.save()

        return redirect('book_author')

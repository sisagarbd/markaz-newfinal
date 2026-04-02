from datetime import date
from django.views.generic import TemplateView
from web_project import TemplateLayout
from apps.book.forms import BookForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from apps.book.models import Author, Catagory, LibraryBranch, Book, Publisher
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




class BookAddView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.add_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))


        context.update(
            {
                "categories": Catagory.objects.all().order_by('id'),
                "publishers": Publisher.objects.all().order_by('id'),
                "authors": Author.objects.all().order_by('id'),
                "libraries": LibraryBranch.objects.all().order_by('id'),
            }
        )
        return context



# class BookAddView(PermissionRequiredMixin, TemplateView):
#     permission_required = ("transactions.add_transaction")

#     def get_context_data(self, **kwargs):
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))

#         def get(self, request):

#             catagories = Catagory.objects.all()


#             context = {
#                 "catagories": catagories,
#             }

#         return redirect("book_add")




### old add with volume

# class BookAddView(PermissionRequiredMixin, TemplateView):
#     permission_required = ("transactions.add_transaction")

#     def get_context_data(self, **kwargs):
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         context['current_date'] = date.today().strftime("%Y-%m-%d")
#         context['authors'] = Author.objects.all()
#         context['libraries'] = LibraryBranch.objects.all()
#         # context['publishers'] = Publisher.objects.all()
#         # context['categories'] = Catagory.objects.all()
#         # context['users'] = User.objects.all()


#         return context


#     @csrf_exempt
#     def ajax_add_author(request):
#         if request.method == "POST":
#             name = request.POST.get("name")

#             author = Author.objects.create(author_name=name)

#             return JsonResponse({
#                 "id": author.id,
#                 "name": author.author_name
#             })




#     def post(self, request):
#         form = BookForm(request.POST)

#         if form.is_valid():

#             total = form.cleaned_data.get("total_volumes")


#             book = form.save(commit=False)
#             book.added_by = request.user
#             book.total_volumes = total
#             book.save()

#             if total and total > 1:

#                 for i in range(1, total + 1):
#                     copy = Book.objects.create(
#                         B_title=f"{book.B_title} - Copy {i}",
#                         author=book.author,
#                         language=book.language,
#                         library=book.library,
#                         total_volumes=1,
#                     )

#             messages.success(request, "Book Added Successfully")
#             return redirect("book_list")

#         print(form.errors)  # ✅ Show errors in terminal
#         messages.error( request, "Book Addition Failed")
#         return redirect("book_add")

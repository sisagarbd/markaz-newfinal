from datetime import date
from urllib import request
from django.views.generic import TemplateView
from web_project import TemplateLayout
from apps.book.forms import BookForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from apps.book.models import Author, Catagory, LibraryBranch, Book, Publisher
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




# class BookAddView(PermissionRequiredMixin, TemplateView):
#     permission_required = ("transactions.add_transaction")

#     def get_context_data(self, **kwargs):
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))


#         context.update(
#             {
#                 "categories": Catagory.objects.all().order_by('id'),
#                 "publishers": Publisher.objects.all().order_by('id'),
#                 "authors": Author.objects.all().order_by('id'),
#                 "libraries": LibraryBranch.objects.all().order_by('id'),
#             }
#         )
#         return context


class BookAddView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.add_transaction")
    template_name = "book/add_book.html"

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

    def post(self, request, *args, **kwargs):

        # 🔹 Basic Fields
        title = request.POST.get("productTitle")
        isbn = request.POST.get("productSku")
        call_no = request.POST.get("productBarcode")
        year = request.POST.get("productyear")
        ddc_no = request.POST.get("ddcNo")

        #GET Image
        book_image = request.FILES.get("book_image")

        # 🔹 Status Fields
        volume = request.POST.get("bookVolume")
        pages = request.POST.get("bookPages")
        edition = request.POST.get("bookEdition")

        # 🔹 Foreign Keys (IMPORTANT)
        catagory_id = request.POST.get("catagory")
        publisher_id = request.POST.get("publisher")
        author_id = request.POST.get("author")
        library_id = request.POST.get("library")

        # 🔹 Checkbox
        is_active = request.POST.get("is_active") == "on"

        # 🔹 Get FK objects
        catagory = Catagory.objects.filter(id=catagory_id).first()
        publisher = Publisher.objects.filter(id=publisher_id).first()
        author = Author.objects.filter(id=author_id).first()
        library = LibraryBranch.objects.filter(id=library_id).first()

        # Library Specific Fields

        shelf_no = request.POST.get("shelfNo")
        added_by = request.POST.get("addedBy")
        date_of_inclusion = request.POST.get("dateInclusion")
        no_of_copy = request.POST.get("noOfCopy")

        print("\n\n\n\n\n\n\n\nReceived Data:")  # ✅ Debugging print statement
        print(pages, shelf_no, added_by, date_of_inclusion, no_of_copy)  # ✅ Debugging print statement
        print("\n\n\n\n\n\n\n\nAll Post")
        print(request.POST)



        # ✅ Create Book
        Book.objects.create(
            B_title=title,
            isbn=isbn,
            call_no=call_no,
            year=year if year else None,
            ddc_no=ddc_no,

            book_image = book_image,


            catagory=catagory,
            publisher=publisher,
            author=author,
            library=library,

            volume=volume if volume else 1,
            pages=pages if pages else None,
            edition=edition if edition else None,

            shelf_no=shelf_no,
            added_by=added_by,
            date_of_inclusion=date_of_inclusion if date_of_inclusion else None,
            no_of_copy=no_of_copy if no_of_copy else 1,

            is_active=is_active
        )

        return redirect('book_list')  # change to your list page



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

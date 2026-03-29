from django.views.generic import TemplateView, DeleteView
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.book.models import Catagory, Author, LibraryBranch
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

#WORKING
class BookLibraryView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        print("Library Branches:", LibraryBranch.objects.all())  # Debugging statement

        context.update(
            {
                "LibraryBranches": LibraryBranch.objects.all().order_by('id'),
            }
        )

        return context




class BookLibraryAdd(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            Library_name = request.POST.get("LibraryName")
            location = request.POST.get("Location")
            city = request.POST.get("City")

            print("Received Data - Library Name:", Library_name, "Location:", location, "City:", city)  # Debugging statement



            LibraryBranch.objects.create(
                Library_name=Library_name, location=location, city=city
            )

            # Catagory.objects.create(catagory_name=catagory_name, slug= slug)
            return redirect('book_library')




class LibraryDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ("transactions.delete_transaction")

    def get(self, request, pk):
        library = get_object_or_404(LibraryBranch, id=pk)
        library.delete()
        messages.success(request, 'Library Deleted')
        return redirect('book_library')









class LibraryEditView(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.delete_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        library = get_object_or_404(LibraryBranch, id=self.kwargs['pk'])
        context['library'] = library

        return context

    def post(self, request, *args, **kwargs):
        library = get_object_or_404(LibraryBranch, id=self.kwargs['pk'])

        library_name = request.POST.get("LibraryName")
        location = request.POST.get("Location")
        city = request.POST.get("City")

        library.Library_name = library_name
        library.location = location
        library.city = city

        library.save()

        return redirect('book_library')

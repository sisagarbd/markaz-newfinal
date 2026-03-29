from django.views.generic import TemplateView, DeleteView
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.book.models import Catagory, Author, LibraryBranch, Publisher
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

#WORKING
class BookPublisherView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        print("Library Branches:", Publisher.objects.all())  # Debugging statement

        context.update(
            {
                "publishers": Publisher.objects.all().order_by('id'),
            }
        )

        return context




class BookPublisherAdd(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            Publisher_name = request.POST.get("Publisher_name")


            print("Received Data - Publisher Name:", Publisher_name)  # Debugging statement



            Publisher.objects.create(
                Publisher_name=Publisher_name
            )

            # Catagory.objects.create(catagory_name=catagory_name, slug= slug)
            return redirect('book_publisher')




class PublisherDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ("transactions.delete_transaction")

    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, id=pk)
        publisher.delete()
        messages.success(request, 'Publisher Deleted')
        return redirect('book_publisher')









class PublisherEditView(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.delete_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        publisher = get_object_or_404(Publisher, id=self.kwargs['pk'])
        context['publisher'] = publisher

        return context

    def post(self, request, *args, **kwargs):
        publisher = get_object_or_404(Publisher, id=self.kwargs['pk'])

        publisher_name = request.POST.get("PublisherName")
        publisher.Publisher_name = publisher_name


        publisher.save()

        return redirect('book_publisher')

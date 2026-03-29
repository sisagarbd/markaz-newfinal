from django.views.generic import TemplateView, DeleteView
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.book.models import Catagory, Author
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages



class BookCatagoryView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context.update(
            {
                "Catagories": Catagory.objects.all().order_by('id'),
            }
        )
        return context

class BookCatagoryAdd(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context


    #  # ✅ THIS IS IMPORTANT
    # def post(self, request, *args, **kwargs):
    #     catagory_name = request.POST.get("categoryTitle")
    #     slug = request.POST.get("catagorySlug")

    #     print("Name:", catagory_name)

    #     Catagory.objects.create(
    #         catagory_name=catagory_name,
    #         slug=slug
    #     )

    #     return redirect('book_catagory')

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            catagory_name = request.POST.get("categoryTitle")
            slug = request.POST.get("catagorySlug")

            Catagory.objects.create(
                catagory_name=catagory_name, slug=slug
            )

            # Catagory.objects.create(catagory_name=catagory_name, slug= slug)
            return redirect('book_catagory')


class CatagoryDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ("transactions.delete_transaction")

    def get(self, request, pk):
        catagory = get_object_or_404(Catagory, id=pk)
        catagory.delete()
        messages.success(request, 'Cagagory Deleted')
        return redirect('book_catagory')





#WORKING
class CatagoryEditView(PermissionRequiredMixin, TemplateView):

    permission_required = ("transactions.delete_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        catagory = get_object_or_404(Catagory, id=self.kwargs['pk'])
        context['catagory'] = catagory

        return context

    def post(self, request, *args, **kwargs):
        catagory = get_object_or_404(Catagory, id=self.kwargs['pk'])

        catagory_name = request.POST.get("categoryTitle")
        slug = request.POST.get("catagorySlug")

        catagory.catagory_name = catagory_name
        catagory.slug = slug
        catagory.save()

        return redirect('book_catagory')







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


class BookLibraryView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "Authors": Author.objects.all().order_by('id'),
            }
        )
        return context


class BookPublisherView(PermissionRequiredMixin, TemplateView):
    permission_required = ("transactions.update_transaction")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "Authors": Author.objects.all().order_by('id'),
            }
        )
        return context

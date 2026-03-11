from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.book.models import Catagory, Author


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

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views import View
from django.urls import reverse_lazy

from inventory.models import Inventory, Manufacturer


class InventoryView(View):
    model = Inventory
    fields = ['part_number', 'alternative_part_number', 'descriptions', 'manufacturer', 'aircraft_type']
    success_url = reverse_lazy('inventory')


class InventoryCreateView(InventoryView, CreateView):
    template_name = "_edit_product.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(deleted_at__isnull=True)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     manufacturers = Manufacturer.objects.all()
    #     context['manufacturers'] = manufacturers
    #     return context

    # def post(self, request, *args, **kwargs):
    #     print(self.request.POST)
    #     self.request.POST.get('part_number')
    #     if self.request.POST.get('kt_invoice_submit_button'):
    #         print('ggggg')
    #     return super().post(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     print(self.request.GET)
    #     return super().get(request, *args, **kwargs)


class InventoryUpdateView(InventoryView, UpdateView):
    template_name = "_edit_product.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(deleted_at__isnull=True)


class InventoryDetailView(InventoryView, DetailView):
    template_name = "_edit_product.html"


class InventoryListView(InventoryView, ListView):
    template_name = "_inventory.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(deleted_at__isnull=True)


class InventoryDeleteView(InventoryView, DeleteView):
    # success_url = reverse_lazy('inventory')
    # paginate_by = 100  # if pagination is desired
    template_name = "inventory_delete.html"

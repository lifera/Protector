from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views import View
from django.urls import reverse_lazy
from inventory.forms import InventoryForm

from inventory.models import Inventory, Manufacturer, AlternativePartNumber
from django.forms import inlineformset_factory


class InventoryView(View):
    model = Inventory
    # fields = ['part_number', 'descriptions', 'manufacturer', 'aircraft_type']
    success_url = reverse_lazy('inventory')
    form_class = InventoryForm


class InventoryCreateView(InventoryView, CreateView):
    template_name = "_edit_product.html"
    AltPartFormSet = inlineformset_factory(Inventory, AlternativePartNumber, fields=('name',))
    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(deleted_at__isnull=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.queryset:
        #     alternative_part_numbers = self.queryset.alternativepartnumber_set.all()
        # else:
        #     alternative_part_numbers = ['1']
        # context['alternative_part_numbers'] = alternative_part_numbers
        print('context')
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        # form = InventoryForm(request.POST, extra=request.POST.get('alt_part_number_count'))
        altformset = self.AltPartFormSet(request.POST, request.FILES)
        # kwargs['form'] = form
        kwargs['altformset'] = altformset
        print(self.request.POST)
        self.request.POST.get('alternative_part_numbers')
        return super().post(request, *args, **kwargs)
    #

    def get(self, request, *args, **kwargs):
        altformset = self.AltPartFormSet()
        kwargs['altformset'] = altformset
        print(self.request.GET)
        # print(self.request.GET.context)
        return super().get(request, *args, **kwargs)


class InventoryUpdateView(InventoryView, UpdateView):
    template_name = "_edit_product.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(deleted_at__isnull=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alternative_part_numbers = AlternativePartNumber.objects.filter(parent_part=self.kwargs['pk'])
        context['alternative_part_numbers'] = alternative_part_numbers
        print('context')
        print(context)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        print('kwargs')
        print(kwargs)
        return kwargs

    def post(self, request, *args, **kwargs):
        form = InventoryForm(request.POST, extra=request.POST.get('alt_part_number_count'))
        kwargs['form'] = form
        print(self.request.POST)
        # if self.request.POST.get('alternative_part_number'):
        #     AlternativePartNumber.objects.create(parent_part_id=self.kwargs['pk'],
        #                                          name=self.request.POST.get('alternative_part_number'))

        return super().post(request, *args, **kwargs)


class InventoryDetailView(InventoryView, DetailView):
    template_name = "_edit_product.html"


class InventoryListView(InventoryView, ListView):
    template_name = "_inventory.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(deleted_at__isnull=True)


class InventoryDeleteView(InventoryView, DeleteView):
    template_name = "inventory_delete.html"

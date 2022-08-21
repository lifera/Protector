from django.forms import ModelForm, CharField, IntegerField, HiddenInput
from inventory.models import Inventory


class InventoryForm(ModelForm):
    # alt_part_number_count = CharField(widget=HiddenInput())

    class Meta:
        model = Inventory
        fields = ['part_number', 'descriptions', 'manufacturer', 'aircraft_type']

    # def __init__(self, *args, **kwargs):
    #     extra_fields = kwargs.pop('extra', 0) if kwargs.pop('extra', 0) is not None else 0
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['alt_part_number_count'].initial = extra_fields
    #     print('extra_fields')
    #     print(extra_fields)
    #     for index in range(int(extra_fields)):
    #         # generate extra fields in the number specified via extra_fields
    #         self.fields['alt_part_number_{index}'.format(index=index)] = CharField()

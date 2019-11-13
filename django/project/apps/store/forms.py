from django.core.exceptions import ValidationError
from django.forms import (
    ModelForm,
    ModelChoiceField,
    Select
)

from . import models


class StoreForm(ModelForm):
    class Meta:
        model = models.Store
        fields = ('name', 'address', 'email')


class ItemForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ('name', 'description')


class StockForm(ModelForm):
    class Meta:
        model = models.Stock
        fields = ('store', 'quantity', 'item')
        widgets = {
            'item': Select(
                attrs={'class': 'form-control'}),
            'store': Select(
                attrs={'class': 'form-control'})
        }

    def __init__(self, user, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        store = self.fields['store']
        store.queryset = models.Store.objects.filter(available=True, user=user)


class PersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = (
            'name',
            'lastName',
            'identification',
            'address',
            'email'
        )


class InvoiceForm(ModelForm):
    class Meta:
        model = models.Invoice
        fields = (
            'number',
            'store',
            'person',
        )

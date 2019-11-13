from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView

from ..utils.views import BaseUpdateView, BaseListView
from . import forms
from . import models


# Create your views here.
class Index(TemplateView):
    http_method_names = ('get')
    template_name = 'store/index.html'


class AddStore(LoginRequiredMixin, CreateView):
    http_method_names = ('get', 'post')
    form_class = forms.StoreForm
    template_name = 'store/store/addStore.html'

    # Add user to 'Store' before commit on save
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class StoreDetail(LoginRequiredMixin, BaseUpdateView):
    form_class = forms.StoreForm
    model = models.Store
    template_name = 'store/store/storeDetail.html'

    # Extra filter for user and his 'Stores'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class StoreList(LoginRequiredMixin, BaseListView):
    model = models.Store
    template_name = 'store/store/storeList.html'

    # Extra filter for user and his 'Stores'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class AddStock(LoginRequiredMixin, CreateView):
    http_method_names = ('get', 'post')
    form_class = forms.StockForm
    template_name = 'store/stock/addStock.html'

    # To send paramter 'user' to the StockForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class StockDetail(LoginRequiredMixin, BaseUpdateView):
    form_class = forms.StockForm
    model = models.Stock
    template_name = 'store/stock/stockDetail.html'

    # To send paramter 'user' to the StockForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    # Extra filter for 'Stores', 'Stocks' and 'User'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(store__user=self.request.user)
        return queryset


class StockList(LoginRequiredMixin, BaseListView):
    model = models.Stock
    template_name = 'store/stock/stockList.html'

    # extra filter
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(store__user=self.request.user)
        return queryset


class AddItem(LoginRequiredMixin, CreateView):
    http_method_names = ('get', 'post')
    form_class = forms.ItemForm
    template_name = 'store/item/addItem.html'


class ItemDetail(LoginRequiredMixin, BaseUpdateView):
    form_class = forms.ItemForm
    model = models.Item
    template_name = 'store/item/itemDetail.html'


class ItemList(LoginRequiredMixin, BaseListView):
    model = models.Item
    template_name = 'store/item/itemList.html'


class AddPerson(LoginRequiredMixin, CreateView):
    http_method_names = ('get', 'post')
    form_class = forms.PersonForm
    template_name = 'store/person/addPerson.html'


class PersonDetail(LoginRequiredMixin, BaseUpdateView):
    form_class = forms.PersonForm
    model = models.Person
    template_name = 'store/person/personDetail.html'


class PersonList(LoginRequiredMixin, BaseListView):
    model = models.Person
    template_name = 'store/person/personList.html'


class AddInvoice(LoginRequiredMixin, CreateView):
    http_method_names = ('get', 'post')
    form_class = forms.InvoiceForm
    template_name = 'store/invoice/addInvoice.html'

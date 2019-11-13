from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Store)
class Store(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'email']
    list_display_links = ['user', 'name']
    search_fields = ['user__username', 'user', 'name', 'email']
    list_filter = ['user', 'available']


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['available']


@admin.register(models.Stock)
class Stock(admin.ModelAdmin):
    list_display = ['store', 'item', 'quantity']
    list_display_links = ['store']
    search_fields = ['store__name', 'store__user', 'store__email', 'item']
    list_filter = ['store', 'available']


@admin.register(models.Person)
class Person(admin.ModelAdmin):
    list_display = ['name', 'lastName', 'identification', 'email']
    list_display_links = ['name', 'lastName', 'identification']
    search_fields = ['name', 'lastName', 'identification', 'email']
    list_filter = ['available']


@admin.register(models.Invoice)
class Invoice(admin.ModelAdmin):
    list_display = ['number', 'store', 'person', 'date']
    list_display_links = ['number']
    search_fields = [
        'number',
        'store__name',
        'person__identification',
        'person__name',
        'person__lastName'
    ]
    list_filter = ['date', 'available']


@admin.register(models.InvoiceDetail)
class InvoiceDetail(admin.ModelAdmin):
    list_display = ['quantity', 'invoice', 'item']
    list_display_links = ['quantity']
    search_fields = [
        'invoice__number',
        'invoice__store',
        'invoice__date',
        'invoice__person__name',
        'invoice__person__lastName',
        'invoice__person__identification'
    ]
    list_filter = ['invoice', 'available']

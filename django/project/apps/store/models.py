from django.db import models
from django.urls import reverse_lazy

from ..utils.models import BaseModel
from ..core.models import User


# Store Information
class Store(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    address = models.TextField(max_length=90)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    def getAbsoluteUrl(self):
        return reverse_lazy('store:storeDetail', kwargs={'id': self.id})

    class Meta:
        ordering = ('name',)


# Product Information
class Item(BaseModel):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=80)

    def __str__(self):
        return self.name

    def getAbsoluteUrl(self):
        return reverse_lazy('store:itemDetail', kwargs={'id': self.id})

    class Meta:
        ordering = ('name', 'description')


# Product Stock
class Stock(BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - quantity: {}'.format(
            self.item.name,
            self.quantity
        )

    def getAbsoluteUrl(self):
        return reverse_lazy('store:stockDetail', kwargs={'id': self.pk})

    class Meta:
        ordering = ('store',)


# Client Information
class Person(BaseModel):
    name = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    identification = models.CharField(max_length=10, unique=True)
    address = models.TextField(max_length=90)
    email = models.EmailField()

    def __str__(self):
        return '{} {} - {}'.format(
            self.name,
            self.lastName,
            self.identification
        )

    def getAbsoluteUrl(self):
        return reverse_lazy('store:personDetail', kwargs={'id': self.pk})

    class Meta:
        ordering = ('name', 'lastName', 'identification')


# Invoice Information
class Invoice(BaseModel):
    number = models.BigIntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    detail = models.ManyToManyField(Item, through='InvoiceDetail')

    def __str__(self):
        return '{} - {} | {}'.format(
            self.number,
            self.person,
            self.date
        )

    def getAbsoluteUrl(self):
        return reverse_lazy('store:invoiceDetail', kwargs={'id': self.pk})

    class Meta:
        ordering = ('store', 'date')


# Weak entity to Invoice
class InvoiceDetail(BaseModel):
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - quantity: {}'.format(
            self.item,
            self.quantity
        )

    def getAbsoluteUrl(self):
        return reverse_lazy('store:invoiceDetailDetail', kwargs={'id': self.pk})

    class Meta:
        ordering = ('invoice__store', 'invoice__date')

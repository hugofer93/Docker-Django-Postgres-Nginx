from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('add/store/', views.AddStore.as_view(), name='addStore'),
    path('store/<int:id>/', views.StoreDetail.as_view(), name='storeDetail'),
    path('store/', views.StoreList.as_view(), name='storeList'),

    path('add/stock/', views.AddStock.as_view(), name='addStock'),
    path('stock/<int:id>/', views.StockDetail.as_view(), name='stockDetail'),
    path('stock/', views.StockList.as_view(), name='stockList'),

    path('add/item/', views.AddItem.as_view(), name='addItem'),
    path('item/<int:id>/', views.ItemDetail.as_view(), name='itemDetail'),
    path('item/', views.ItemList.as_view(), name='itemList'),

    path('add/client/', views.AddPerson.as_view(), name='addPerson'),
    path('client/<int:id>/', views.PersonDetail.as_view(), name='personDetail'),
    path('client/', views.PersonList.as_view(), name='personList'),

    path('add/sale/', views.AddInvoice.as_view(), name='addInvoice'),
    #path('sale/<int:id>/', views.InvoiceDetail.as_view(), name='invoiceDetail'),
    #path('sale/', views.InvoiceList.as_view(), name='invoiceList'),
]

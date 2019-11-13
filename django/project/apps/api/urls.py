from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('store/', views.Store.as_view(), name='store'),
    path('store/<int:id>/', views.StoreDetail.as_view(), name='storeDetail'),

    path('stock/', views.Stock.as_view(), name='stock'),
    path('stock/<int:id>/', views.StockDetail.as_view(), name='stockDetail'),

    path('item/', views.Item.as_view(), name='item'),
    path('item/<int:id>/', views.ItemDetail.as_view(), name='itemDetail'),

    path('person/', views.Person.as_view(), name='person'),
    path('person/<int:id>/', views.PersonDetail.as_view(), name='personDetail'),
]

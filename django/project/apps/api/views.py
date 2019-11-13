from rest_framework.response import Response

from ..utils.views import (
    BaseGetPostList,
    BaseGetPutPatchDeleteDetail
)
from .models import modelsStoreApp
from . import serializers


class Store(BaseGetPostList):
    serializer_class = serializers.StoreSerializer
    queryset = modelsStoreApp.Store.objects.all()

    # Validation for method 'GET'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    # Validation for method 'POST' in new Store for user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoreDetail(BaseGetPutPatchDeleteDetail):
    serializer_class = serializers.StoreSerializer
    queryset = modelsStoreApp.Store.objects.all()

    # Validation for 'get_object' (methods: 'GET', 'PUT', 'PATCH', 'DELETE')
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class Stock(BaseGetPostList):
    serializer_class = serializers.StockSerializer
    queryset = modelsStoreApp.Stock.objects.all()

    # Validation for method 'GET'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(store__user=self.request.user)
        return queryset


class StockDetail(BaseGetPutPatchDeleteDetail):
    serializer_class = serializers.StockSerializer
    queryset = modelsStoreApp.Stock.objects.all()

    # Validation for 'get_object' (methods: 'GET', 'PUT', 'PATCH', 'DELETE')
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(store__user=self.request.user)
        return queryset


class Item(BaseGetPostList):
    serializer_class = serializers.ItemSerializer
    queryset = modelsStoreApp.Item.objects.all()


class ItemDetail(BaseGetPutPatchDeleteDetail):
    serializer_class = serializers.ItemSerializer
    queryset = modelsStoreApp.Stock.objects.all()


class Person(BaseGetPostList):
    serializer_class = serializers.PersonSerializer
    queryset = modelsStoreApp.Person.objects.all()


class PersonDetail(BaseGetPutPatchDeleteDetail):
    serializer_class = serializers.PersonSerializer
    queryset = modelsStoreApp.Person.objects.all()

'''
NOTE: for reasons of time use 'ModelSerializer',
it is highly recommended to use 'Serializer',
to improve performance.
'''

from rest_framework.serializers import ModelSerializer, ValidationError

from .models import modelsStoreApp


class StoreSerializer(ModelSerializer):
    class Meta:
        model = modelsStoreApp.Store
        fields = ('id', 'name', 'address', 'email')


class StockSerializer(ModelSerializer):
    class Meta:
        model = modelsStoreApp.Stock
        fields = ('id', 'store', 'quantity', 'item')

    # Valitation for User's Store
    def validate_store(self, value):
        user = self.context.get('request').user
        userStores = modelsStoreApp.Store.objects.filter(
            available=True,
            user=user
        )
        if value not in userStores:
            raise ValidationError("Invalid store.")
        return value


class ItemSerializer(ModelSerializer):
    class Meta:
        model = modelsStoreApp.Item
        fields = ('id', 'name', 'description')


class PersonSerializer(ModelSerializer):
    class Meta:
        model = modelsStoreApp.Person
        fields = (
            'id',
            'name',
            'lastName',
            'identification',
            'address',
            'email'
        )


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = modelsStoreApp.Invoice
        fields = (
            'id',
            'number',
            'store',
            'person',
            'detail'
        )

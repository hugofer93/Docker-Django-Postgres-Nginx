from django.core.exceptions import ImproperlyConfigured
from django.views.generic import UpdateView, ListView

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Model


# Update View for project
class BaseUpdateView(UpdateView):
    http_method_names = ('get', 'post')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(available=True)
        return queryset


# List View for project
class BaseListView(ListView):
    http_method_names = ('get')
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(available=True)
        return queryset


# BASE CLASS FOR API (LIST: GET, POST)
class BaseGetPostList(ListCreateAPIView):
    # Validation for method 'GET'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(available=True)
        return queryset


# BASE CLASS FOR API (DETAIL: GET, PUT, PATCH, DELETE)
class BaseGetPutPatchDeleteDetail(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'

    # Validation for 'get_object' (methods: 'GET', 'PUT', 'PATCH', 'DELETE')
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(available=True)
        return queryset

    # Extra validation for method 'DELETE'
    def perform_destroy(self, instance):
        instance.available = False # Logical erasure
        instance.save()

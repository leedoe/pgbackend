from rest_framework import viewsets

from ..models import Store
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filterset_fields = {
        'x': ['gte', 'lte'],
        'y': ['gte', 'lte'],
        'category': ['exact']
    }

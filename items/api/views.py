from items.api.paginations import ItemsSetPagination
from items.api.serializers import ItemSerializer, LeatherSerializer
from rest_framework import mixins, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from items.models import Item, Leather


class ItemListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = ItemsSetPagination
    queryset = Item.objects.filter(soldout=False).order_by('price')
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    # filterset_fields = ['name']
    search_fields = ['name']
    

class LeatherViewset(viewsets.ModelViewSet):
    queryset = Leather.objects.all()
    serializer_class = LeatherSerializer
    
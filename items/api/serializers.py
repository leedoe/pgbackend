from rest_framework import serializers
from rest_framework import fields

from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'name',
            'thumbnail',
            'price',
            'link',
            'soldout',
            'store_name'
        ]

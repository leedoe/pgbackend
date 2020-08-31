from stores.api.serializers import StoreSerializer
from rest_framework import serializers
from rest_framework import fields

from items.models import Item, Leather, LeatherDetail, Material, Tannery


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


class LeatherDetailSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    class Meta:
        model = LeatherDetail
        fields = [
            'store',
            'price',
            'note'
        ]


class TannerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tannery
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class LeatherSerializer(serializers.ModelSerializer):
    tannery = TannerySerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    leather_details = LeatherDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Leather
        fields = [
            'pk',
            'name',
            'tannery',
            'material',
            'explanation',
            'leather_details',
            # 'shop_name'
        ]
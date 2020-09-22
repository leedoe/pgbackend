from utils.s3.s3 import upload_file
from stores.api.serializers import StoreSerializer
from rest_framework import serializers
from rest_framework import fields

from items.models import Comment, Item, Leather, LeatherDetail, Material, Tannery


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
        fields = '__all__'


class LeatherDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeatherDetail
        fields = '__all__'


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
            'image',
            'name',
            'tanning_method',
            'tannery',
            'material',
            'explanation',
            'leather_details',
            # 'shop_name'
        ]


class LeatherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leather
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
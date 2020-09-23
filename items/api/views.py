from rest_framework import serializers
from items.api.paginations import ItemsSetPagination
from items.api.serializers import CommentSerializer, ItemSerializer, LeatherCreateSerializer, LeatherDetailCreateSerializer, LeatherDetailSerializer, LeatherSerializer, MaterialSerializer, TannerySerializer
from rest_framework import mixins, viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from items.models import Item, Leather, LeatherDetail, Material, Tannery, Comment

from utils.s3.s3 import upload_file

import json


class ItemListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = ItemsSetPagination
    queryset = Item.objects.filter(soldout=False).order_by('price')
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    # filterset_fields = ['name']
    search_fields = ['name']
    

class LeatherViewset(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Leather.objects.all()
    serializer_class = LeatherSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['writer'] = request.user.pk
        try:
            url = upload_file(request.FILES['image'].file)
            data['image'] = url
        except Exception:
            data['image'] = None

        serializer = LeatherCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TanneryViewset(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Tannery.objects.all()
    serializer_class = TannerySerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['writer'] = request.user.pk
        try:
            url = upload_file(request.FILES['logo'].file)
            data['logo'] = url
        except Exception:
            data['logo'] = None
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class MaterialViewset(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['writer'] = request.user.pk
        try:
            url = upload_file(request.FILES['image'].file)
            data['image'] = url
        except Exception:
            data['image'] = None
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentViewset(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Comment.objects.filter(deleted=False).order_by('created_time')
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division', 'fk']

    def destroy(self, request, pk=None):
        instance = self.get_object()
        if instance.password is not None:
            if request.data['password'] == instance.password:
                instance.deleted = True
                instance.save()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            if request.user == instance.writer:
                instance.deleted = True
                instance.save()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        # instance.deleted = True
        # instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LeatherDetailViewset(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = LeatherDetail.objects.all()
    # serializer_class = LeatherDetailCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return LeatherDetailCreateSerializer
        else:
            return LeatherDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['writer'] = request.user.pk
        try:
            url = upload_file(request.FILES['image'].file)
            data['image'] = url
        except Exception:
            data['image'] = None
            
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
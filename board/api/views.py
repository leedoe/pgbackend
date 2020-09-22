import base64
import boto3
import uuid
import json
import environ

from django.db.models import Count
from django.db.models.query_utils import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from board.models import Category, Comment, Post

from .serializers import CategorySerializer, CommentSerializer, PostListSerializer, PostRetrieveSerializer, PostSerializer
from .permissions import IsWriterOnly
from .paginations import PostsSetPagination


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsWriterOnly,)
    queryset = Comment.objects.filter(deleted=False).order_by('created_time')
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def list(self, request, *arg, **kwargs):
        if request.query_params.dict() == {}:
            raise NotFound()

        return super(CommentViewSet, self).list(self, request, *arg, **kwargs)


class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostsSetPagination
    permission_classes = (IsWriterOnly,)
    queryset = Post.objects.filter(deleted=False) \
        .annotate(comment_count=Count('comment', filter=Q(comment__deleted=False))) \
        .order_by('-created_time')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['noticed']
    search_fields = ['content', 'writer_name', 'comment__content']

    def get_queryset(self):
        if self.action == 'list':
            if self.request.query_params.get('category__name', None) is None:
                queryset = Post.objects.filter(deleted=False) \
                    .exclude(category__name='건의') \
                    .annotate(comment_count=Count('comment', filter=Q(comment__deleted=False))) \
                    .order_by('-created_time')
            else:
                queryset = Post.objects.filter(deleted=False, category__name='건의') \
                    .annotate(comment_count=Count('comment', filter=Q(comment__deleted=False))) \
                    .order_by('-created_time')
        else:
            queryset = Post.objects.filter(deleted=False) \
                    .annotate(comment_count=Count('comment', filter=Q(comment__deleted=False))) \
                    .order_by('-created_time')

        return queryset

    def making_object(bucket_name, base64):
        env = environ.Env()
        key = f'{str(uuid.uuid4())}.jpg'
        client = boto3.client(
            's3',
            aws_access_key_id=env('aws_access_key_id'),
            aws_secret_access_key=env('aws_secret_access_key')
            )
        client.put_object(
            Bucket='leatherleather',
            Body=base64,
            Key=key,
            ContentType='image/jpg'
        )

        url = f'https://leatherleather.s3.ap-northeast-2.amazonaws.com/{key}'
        return url

    def base642Image(self, content):
        for index in content['entityMap']:
            if content['entityMap'][index]['type'] == 'img':
                base64image = content['entityMap'][index]['data']['src']
                startIndex = base64image.find('base64,')
                base64String = base64image[startIndex+7:]
                try:
                    imgdata = base64.b64decode(base64String)
                except Exception:
                    continue
                url = self.making_object(imgdata)
                content['entityMap'][index]['data']['src'] = url

        return content

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostRetrieveSerializer
        else:
            return self.serializer_class

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        instance.views += 1
        serializer = self.get_serializer(instance, data=instance.__dict__)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        content = request.data['content']

        content = self.base642Image(content)

        request.data['content'] = content
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        content = request.data['content']
        content = self.base642Image(content)
        request.data['content'] = content

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class CategoryViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
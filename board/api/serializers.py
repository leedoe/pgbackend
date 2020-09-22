from rest_framework import serializers

from board.models import Category, Comment, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'pk',
            'parent',
            'post',
            'content',
            'writer_name',
            'writer',
            'created_time',
            'deleted'
        ]
        extra_kwargs = {
            'deleted': {'write_only': True}
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'content',
            'password',
            'writer_name',
            'writer',
            'category',
            'noticed',
            'created_time',
            'views',
            'deleted'
        ]


class PostListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField()

    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'writer_name',
            'noticed',
            'category',
            'created_time',
            'views',
            'comment_count'
        ]


class PostRetrieveSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'content',
            'writer_name',
            'writer',
            'noticed',
            'category',
            'created_time',
            'views'
        ]


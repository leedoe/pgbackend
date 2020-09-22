from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=191, unique=True)

    def __str__(self):
        return f'{self.name}'


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=191)
    content = models.JSONField()
    writer_name = models.CharField(max_length=191)
    password = models.CharField(max_length=100, null=True, blank=True)
    writer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    noticed = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True)
    deleted = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    writer_name = models.CharField(max_length=191)
    password = models.CharField(max_length=100, null=True, blank=True)
    writer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post}, {self.content}'

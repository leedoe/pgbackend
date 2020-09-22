from django.db import models

from stores.models import Store
from users.models import User


class Item(models.Model):
    name = models.CharField(max_length=300)
    thumbnail = models.URLField(max_length=300)
    price = models.IntegerField()
    link = models.URLField(max_length=300)
    soldout = models.BooleanField()
    store_name = models.CharField(max_length=191)


class Tannery(models.Model):
    logo = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100)
    explanation = models.TextField(null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    image = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=100)
    explanation = models.TextField(null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Leather(models.Model):
    TANNING_METHOD = [
        (0, 'Vegetable'),
        (1, 'Chrome'),
        (2, 'Hybrid')
    ]

    image = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=150)
    tannery = models.ForeignKey(Tannery, on_delete=models.CASCADE, null=True, blank=True)
    tanning_method = models.IntegerField(choices=TANNING_METHOD)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    explanation = models.TextField(null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LeatherDetail(models.Model):
    image = models.URLField(null=True, blank=True)
    leather = models.ForeignKey(
        Leather,
        on_delete=models.CASCADE,
        related_name='leather_details')
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        limit_choices_to={'category': 2})
    price = models.IntegerField()
    sellingPageUrl = models.URLField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    DIVISION = [
        (0, 'Tannery'),
        (1, 'Material'),
        (2, 'Leather'),
        (3, 'LeatherDetail')
    ]

    division = models.IntegerField(choices=DIVISION)
    fk = models.IntegerField()
    writer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='writer')
    writer_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, null=True, blank=True)
    content = models.JSONField()
    deleted = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
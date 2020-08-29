from django.db import models
from django.db.models.deletion import CASCADE

from stores.models import Store


class Item(models.Model):
    name = models.CharField(max_length=300)
    thumbnail = models.URLField(max_length=300)
    price = models.IntegerField()
    link = models.URLField(max_length=300)
    soldout = models.BooleanField()
    store_name = models.CharField(max_length=191)


class Tannery(models.Model):
    name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100)
    explanation = models.TextField()


class Material(models.Model):
    name = models.CharField(max_length=100)
    explanation = models.TextField()


class Leather(models.Model):
    TANNING_METHOD = [
        (0, 'Vegetable'),
        (1, 'Chrome'),
        (2, 'Hybrid')
    ]

    name = models.CharField(max_length=150)
    tanery = models.ForeignKey(Tannery, on_delete=models.CASCADE)
    tanning_method = models.IntegerField(choices=TANNING_METHOD)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    explanation = models.TextField()


class LeatherDetail(models.Model):
    leather = models.ForeignKey(Leather, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.IntegerField()
    note = models.TextField()

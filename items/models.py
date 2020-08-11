from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=300)
    thumbnail = models.URLField(max_length=300)
    price = models.IntegerField()
    link = models.URLField(max_length=300)
    soldout = models.BooleanField()
    store_name = models.CharField(max_length=191)
from django.db import models


# Create your models here.
class Store(models.Model):
    CATEGORIES = [
        (0, 'workshop'),
        (1, 'toolStore'),
        (2, 'leatherStore'),
        (3, 'commonStore'),
        (4, 'materialStore')
    ]

    name = models.CharField(max_length=191)
    x = models.CharField(max_length=20)
    y = models.CharField(max_length=20)
    address = models.CharField(max_length=191)
    category = models.IntegerField(choices=CATEGORIES)
    homepage = models.URLField(null=True, blank=True, max_length=300)
    blog = models.URLField(null=True, blank=True, max_length=300)
    instagram = models.URLField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.name

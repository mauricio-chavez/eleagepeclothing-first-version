from django.db import models

import os

from django.utils import timezone

def get_image_path(instance, filename):
    return os.path.join('items_images', str(instance.id), filename)

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    pub_date = models.DateField('date published',default=timezone.now)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, max_length=200,null=True)
    category = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    pass
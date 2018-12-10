from django.db import models

import os

from django.utils import timezone

SIZES = (
    ('xs','Extra Chica'),
    ('s', 'Chica'),
    ('m', 'Mediana'),
    ('l', 'Grande'),
    ('xl', 'Extra grande'),
)

def get_image_path(instance, filename):
    return os.path.join('items_images', str(instance.id), filename)

class Size(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=6)

    def get_choices_form(self):
        return (self.abbreviation, self.name)

    def __str__(self):
        return self.name + ' (' + self.abbreviation + ')'

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    pub_date = models.DateField('date published',default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_sizes = models.ManyToManyField('Size')
    short_description = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, max_length=200,null=True)
    category = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.name

    def get_available_sizes(self):
        ls = []
        for size in self.available_sizes.all():
            ls.append(size.get_choices_form())
        return ls




    
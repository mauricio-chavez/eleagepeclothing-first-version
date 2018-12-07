from django.db import models

import os

from django.contrib.auth.models import User

from django.utils import timezone

from shop.models import Item

def get_image_path_shop_user(instance, filename):
    return os.path.join('profile_pictures', str(instance.id), filename)

def get_default_profile_picture():
    return os.path.join('profile_pictures', 'default.png')

class ShopUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=get_image_path_shop_user, default=get_default_profile_picture,max_length=200)
    order_history = models.ManyToManyField('ShoppingCart',blank=True)

    def __str__(self):
       return '@' + str(self.user)

class ShoppingCart(models.Model):
    user = models.OneToOneField('ShopUser', blank=True, null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,blank=True)
    prices_sum = models.DecimalField(max_digits=10, blank=True, decimal_places=2, default=0)
    bought = models.BooleanField(blank=True,default=False)
    date = models.DateField(blank=True,default=timezone.now)

    def sum_prices(self):
        self.prices_sum = 0
        for item in self.items.all():
            self.prices_sum += item.price

        self.save()

    def __str__(self):
        if self.user is not None:
            return self.user.username + "'s shopping cart -- $" + str(self.prices_sum)
        else:
            return "Somebody's shopping cart -- $" + str(self.prices_sum)

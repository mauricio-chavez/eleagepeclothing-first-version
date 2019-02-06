import os

from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db import models
from django.dispatch import receiver
from django.utils import timezone

from shop.models import Item, Size

@receiver(pre_save, sender='users.ShoppingCart')
def sum_price(sender, instance, **kwargs):
    instance.sum_prices()

def get_image_path_shop_user(instance, filename):
    return os.path.join('profile_pictures', str(instance.id), filename)

def get_default_profile_picture():
    return os.path.join('profile_pictures', 'default.png')

class ShopUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=get_image_path_shop_user, default=get_default_profile_picture,max_length=200)
    shopping_cart = models.OneToOneField('ShoppingCart', null=True, blank=True , on_delete=models.SET_NULL)

    def __str__(self):
       return '@' + str(self.user)

class ShopItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.PROTECT, null=True)
    quantity = models.IntegerField('Cantidad')

class ShoppingCart(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    prices_sum = models.DecimalField(max_digits=10, blank=True, decimal_places=2, default=0)
    bought = models.BooleanField(blank=True,default=False)
    date = models.DateField(auto_now=True)

    def sum_prices(self):
        self.prices_sum = 0
        for item in self.items.all():
            self.prices_sum += item.price

    def add_item(self, item):
        self.items.add(item)
        self.save()
    
    def count_items(self):
        """
        items = 0
        for _ in self.items.all():
            items += 1
        return items
        """
        return len(self.items.all())

    def __str__(self):
        return "Shopping cart -- $" + str(self.prices_sum)

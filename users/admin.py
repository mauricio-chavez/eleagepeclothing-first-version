from django.contrib import admin

from .models import ShopUser, ShoppingCart

admin.site.register(ShopUser)
admin.site.register(ShoppingCart)

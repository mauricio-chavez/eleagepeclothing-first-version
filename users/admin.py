from django.contrib import admin

from .models import ShopUser, ShoppingCart, ShopItem

admin.site.register(ShopUser)
admin.site.register(ShopItem)
admin.site.register(ShoppingCart)

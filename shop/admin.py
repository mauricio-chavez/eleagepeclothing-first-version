from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Item, Category, Size

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Size)


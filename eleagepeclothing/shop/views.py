from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse

from .models import Item
from users.models import ShopUser

def shop(request):
    items = Item.objects.all()
    item_list = []
    count = 0
    while count <= len(items):
        item_tuple = tuple(items[count:count+3])
        count += 3
        item_list.append(item_tuple)

    return render(request, 'shop/shop.html', {'item_list': item_list})

def detail(request, id):
    item = get_object_or_404(Item,id=id)
                    
    return render(request, 'shop/details.html', {'item' : item})

"""
@login_required(login_url='')
def my_view(request):
"""
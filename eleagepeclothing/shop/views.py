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
    if request.user.is_authenticated:
        user = ShopUser.objects.get(user=request.user)
        username = request.user.first_name if request.user.first_name != "" else "@" + request.user.username
        context = { 'base': 'shop/base_logged.html',
                    'user': user,
                    'username': username,
                    'item_list': item_list}
    else:
        context = { 'base': 'shop/base.html',
                    'item_list': item_list}
    return render(request, 'shop/shop.html', context)

def detail(request, id):
    item = get_object_or_404(Item,id=id)
    if request.user.is_authenticated:
        user = ShopUser.objects.get(user=request.user)
        username = request.user.first_name if request.user.first_name != "" else request.user.username
        context = { 'base': 'shop/base_logged.html',
                    'user': user,
                    'username': username,
                    'item' : item }
    else:
        context = { 'base': 'shop/base.html',
                    'item' : item}
    return render(request, 'shop/details.html', context)

"""
@login_required(login_url='')
def my_view(request):
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse

from .models import Item
from users.models import ShopUser, ShoppingCart

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
                    
    return render(request, 'shop/details.html', {'item' : item } )

@login_required
def add_to_cart(request):
    user = ShopUser.objects.get(user=request.user)
    if user.shopping_cart:
        item_id = request.POST['item_id']
        user.shopping_cart.add_item(Item.objects.get(id=item_id))
    else:
        cart = ShoppingCart()
        cart.save()
        user.shopping_cart = cart
        user.save()

        item_id = request.POST['item_id']
        user.shopping_cart.add_item(Item.objects.get(id=item_id))
    return redirect('detail',item_id)
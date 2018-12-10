from users.models import ShopUser

def item_count(request):
    """
    if request.user.is_authenticated:
        shop_user = ShopUser.objects.get(user=request.user)
        if shop_user:
            if shop_user.shopping_cart:
                return {'item_count': shop_user.shopping_cart.count_items()}
            else:
                return {}
        else:
            return {}
    else:
        return {}
    """
    if request.user.is_authenticated:
        shop_user = ShopUser.objects.get(user=request.user)
        if shop_user and shop_user.shopping_cart:
            return {'item_count': shop_user.shopping_cart.count_items()}
        else:
            return {}
    else:
        return {}

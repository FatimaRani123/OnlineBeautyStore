from .utils import get_cart

def cart_item_count(request):
    cart = get_cart(request)
    return {'cart_item_count': cart.items.count() if cart else 0}

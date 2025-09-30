from .cart import Cart


def display_cart(request):
    return {"cart": Cart(request)}

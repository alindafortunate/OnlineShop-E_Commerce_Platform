from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.session = request.session
        # Getting the cart from the current session.
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price),
            }
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

    def save(self):
        # Mark the session as modified to make sure it gets saved.
        self.session.modified = True

    def remove(self, product):
        """
        Remove the product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]

        self.save()

    def __iter__(self):
        """
        Iterate over the objects in the cart and get the products from the database.
        """
        product_ids = self.cart.keys()
        # Get products from the database
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]

        yield item

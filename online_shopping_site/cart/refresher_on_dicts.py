# Refreshing my mind on dictionaries.


class Shopping_Cart:
    def __init__(self):
        self.cart = {}

    def add_item(self, product_id, quantity, price, name):
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": price,
                "name": name,
            }
        self.cart[product_id]["quantity"] += quantity

    def total_items(self):
        total = 0
        for product_id in self.cart:
            total += self.cart[product_id]["quantity"]
        return total

    def total_price(self):
        price = 0
        for product_id in self.cart:
            price += self.cart[product_id]["price"]
        return price


alinda_Shopping_Cart = Shopping_Cart()
alinda_Shopping_Cart.add_item(1, 3, 2300, "tomatoes")
alinda_Shopping_Cart.add_item(2, 4, 2500, "apples")
alinda_Shopping_Cart.add_item(6, 3, 2800, "oranges")
total = alinda_Shopping_Cart.total_items()
print(f"{total} items")
print(alinda_Shopping_Cart.cart)
print(alinda_Shopping_Cart.total_price())

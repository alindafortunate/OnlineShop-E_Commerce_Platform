from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            # clear the cart.
            cart.clear()
            # Launch an asychronous order_created task
            # order_created.delay(order.id) # Due to render deployment I am not able to use RabbitMQ so I have commented out this line.
        return render(request, "orders/order/created.html", {"order": order})
    else:
        form = OrderCreateForm()
        return render(request, "orders/order/create.html", {"cart": cart, "form": form})


# On 16th/10/2025 I installed RabbitMQ

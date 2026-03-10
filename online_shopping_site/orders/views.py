from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Order, OrderItem
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
            # order_created.delay(
            #     order.id
            # )  # Due to render deployment I am not able to use RabbitMQ so I have commented out this line.
            # Set the order in the session.
            request.session["order_id"] = order.id
            # redirect for payment
            return redirect("payment:process")
    else:
        form = OrderCreateForm()
        return render(request, "orders/order/create.html", {"cart": cart, "form": form})


# On 16th/10/2025 I installed RabbitMQ
# On 14th/11/2025 I resumed coding after the period of inactivity.
# On 12th/Dec/2025 I switched the machine for programming and by 13th/Dec/2025 after lunch time I was almost completing


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})

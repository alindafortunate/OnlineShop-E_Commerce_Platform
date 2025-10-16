from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_create(order_id):
    """
    Task to send an email notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order number:{order.id}"
    message = f"Dear {order.first_name}, thank your placing an order. \n\n Your order {order.id} was successful."
    mail_sent = send_mail(
        subject,
        message,
        "alindafortunate5@gmail.com",
        [order.email],
    )
    return mail_sent

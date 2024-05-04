from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from products.models import Product


SHIPMENT_METHODS = {
    'sdek': 'CDEK',
    'mail': 'Почта',
}

STATUSES = {
    'pending': 'Pending',
    'paid': 'Paid',
    'canceled': 'Canceled',
    'failed': 'Failed',
}


class Order(models.Model):
    client_name = models.CharField(max_length=120)
    client_phone = PhoneNumberField()
    shipment_method = models.CharField(
        max_length=10,
        choices=SHIPMENT_METHODS
    )
    status = models.CharField(
        max_length=10,
        choices=STATUSES
    )

    class Meta:
        db_table = 'orders'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    image = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'order_products'


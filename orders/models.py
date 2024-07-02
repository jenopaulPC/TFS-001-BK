from django.db import models
from user.models import *
from products.models import *

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f' {self.user}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class ShippingAddress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'Shipping address for order {self.order.id}'
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('PayPal', 'PayPal'), ('Net Banking', 'Net Banking')])
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment for order {self.order.id}'
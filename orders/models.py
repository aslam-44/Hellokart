from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    LIVE = 1
    DELETE = 0

    DELETE_CHOICES = [
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    ]
    CART_STAGE = 0
    ORDER_CONFIMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = (
        (ORDER_PROCESSED, "ORDER_PROCESSED")
        (ORDER_DELIVERED, "ORDER_DELIVERED")
        (ORDER_REJECTED, "ORDER_REJECTED")
    )
    order_status = models.IntegerField(choices=STATUS_CHOICES , default= CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name="orders", null=True)
    address = models.TextField()  
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="user_profile")  
    phone = models.CharField(max_length=10)
    priority = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Order by {self.owner} at {self.created_at}"

class OrderItem(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="added_carts", null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="added_items")

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

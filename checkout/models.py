"""based on Botique Ado walkthrough project"""

import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from courses.models import Course

# Create your models here.
class Order(models.Model):
    """handles all orders across the site"""
    order_number = models.CharField(max_length=50, null=False, editable=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    second_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    address1 = models.CharField(max_length=60, null=False, blank=False)
    address2 = models.CharField(max_length=60, null=True, blank=True)
    region_or_county = models.CharField(max_length=60, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _create_order_number(self):
        """randomly creates a unique order number"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """updates grand total each time an item is added"""
        self.order_total = self.orderitems.aggregate(Sum('orderitem_total'))['orderitem_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        """overrides existing save method, 
        sets order number if not already set"""
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number




class OrderItem(models.Model):
    """handles specific items in the shopping bag"""
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems')
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """overrides existing save method, set, orderitem total
        and updates order total"""
        self.orderitem_total = self.course.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'SKU {self.course.sku} for order {self.order.order_number}'

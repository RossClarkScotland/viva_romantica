"""based on Botique Ado walkthrough project"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def update_upon_saving(sender, instance, created, **kwargs):
    """necessary to handle post_save signals,
    updates order total whenever an item is 
    updated or created"""
    instance.order.update_total()

@receiver(post_delete, sender=OrderItem)
def delete_upon_saving(sender, instance, **kwargs):
    """necessary to handle post_delete signals,
    updates order total whenever an item is 
    deleted"""
    instance.order.update_total()
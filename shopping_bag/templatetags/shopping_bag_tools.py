from django import template
"""as shown in Boutique Ado walkthrough project"""
register = template.Library()

@register.filter(name='shopping_bag_tools')
def calculate_subtotal(price, quantity):
    return price * quantity
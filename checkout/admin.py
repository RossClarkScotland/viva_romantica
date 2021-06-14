from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemAdminInline(admin.TabularInline):
    """enables superuser to add/edit individual order items in the admin"""
    model = OrderItem
    readonly_fields = ('orderitem_total',)

class OrderAdministration(admin.ModelAdmin):
    """sets up the admin page for the checkout"""
    
    inlines = (OrderItemAdminInline,)

    """establishes fields which cannot be altered"""
    readonly_fields = ('order_number', 'date', 'order_total', 'grand_total',)

    """specifies the order in which fields appear in admin"""
    fields = ('order_number', 'date', 'first_name', 'second_name', 
              'order_total', 'grand_total', 'email', 'phone_number', 
              'country', 'postcode', 'town_or_city', 'address1', 
              'address2', 'region_or_county',)
    
    """specifies which elements appear in the order list"""
    list_display = ('order_number', 'date', 'first_name', 'second_name',
                    'order_total', 'grand_total',)
    
    """displays the most recent orders first"""
    ordering = ('-date',)

admin.site.register(Order, OrderAdministration)
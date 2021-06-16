# Based on Boutique Ado walkthrough project
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here
def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "Your shopping bag is currently empty")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J2jhOBsZwD5BzE8wyRJYa4tDBYik8umWwqV6KqmNOMde6HRryTqzVChPFK9ukAVWEYqmNCvB038vABPvAS1zIAN00xbOtfXxJ',
        'client_secret': 'test',
    }

    return render(request, template, context)
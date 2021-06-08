from django.shortcuts import render

# Create your views here.
def view_shopping_bag(request):
    """renders shopping bag page"""

    return render(request, 'shopping_bag/shopping_bag.html')
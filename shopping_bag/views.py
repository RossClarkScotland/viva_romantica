from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from courses.models import Course

# Create your views here.
def view_shopping_bag(request):
    """renders shopping bag page"""

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add courses to the shopping bag """

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
        messages.success(request, f'You updated the quantity of {course.name} in your shopping bag!')
    else:
        shopping_bag[item_id] = quantity
        messages.success(request, f'You added {course.name} to your bag!')


    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(redirect_url)


def change_shopping_bag(request, item_id):
    """ changes number of courses in the shopping bag """

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 0:
        shopping_bag[item_id] = quantity
        messages.success(request, f'You updated the quantity of {course.name} in your shopping bag!')
    else:
        shopping_bag.pop(item_id)
        messages.success(request, f'You removed {course.name} from your shopping bag!')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse(view_shopping_bag))


def remove_from_shopping_bag(request, item_id):
    """removes items from shopping bag"""

    try:
        course = get_object_or_404(Course, pk=item_id)
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag.pop(item_id)
        messages.success(request, f'You removed {course.name} from your shopping bag!')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'There was an error in removing the item {e}')
        return HttpResponse(status=500)
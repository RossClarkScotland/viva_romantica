from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course

def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    grand_total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, quantity in shopping_bag.items():
        course = get_object_or_404(Course, pk=item_id)
        total += quantity * course.price
        product_count += quantity
        shopping_bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'course': course,
        })

    if total >= settings.COURSE_DISCOUNT_POINT:
        grand_total = total - 20
    else: 
        grand_total = total


    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'course_discount_point': settings.COURSE_DISCOUNT_POINT,
    }

    return context
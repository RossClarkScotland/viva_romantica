from django.conf import settings

def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    grand_total = 0
    product_count = 0

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
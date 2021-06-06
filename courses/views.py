from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.
def spanish_courses(request):
    """shows Spanish courses"""

    spanish_courses = Course.objects.filter(name__contains='Spanish')

    context = {
        'spanish_courses': spanish_courses,
    }

    return render(request, 'courses/spanish.html', context)

  
def italian_courses(request):
    """shows Italian courses"""

    italian_courses = Course.objects.filter(name__contains='Italian')

    context = {
        'italian_courses': italian_courses,
    }

    return render(request, 'courses/italian.html', context)


def french_courses(request):
    """shows French courses"""

    french_courses = Course.objects.filter(name__contains='French')

    context = {
        'french_courses': french_courses,
    }

    return render(request, 'courses/french.html', context)


def portugese_courses(request):
    """shows Portugese courses"""

    portugese_courses = Course.objects.filter(name__contains='Portugese')

    context = {
        'portugese_courses': portugese_courses,
    }

    return render(request, 'courses/portugese.html', context)


def romanian_courses(request):
    """shows Romanian courses"""

    romanian_courses = Course.objects.filter(name__contains='Romanian')

    context = {
        'romanian_courses': romanian_courses,
    }

    return render(request, 'courses/romanian.html', context)


def course_details(request, course_id):
    """gives details on individual courses"""

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_details.html', context)

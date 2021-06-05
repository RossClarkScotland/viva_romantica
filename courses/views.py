from django.shortcuts import render
from .models import Course

# Create your views here.
def all_courses(request):
    """shows all courses"""

    courses = Course.objects.all()
    spanish_courses = Course.objects.filter(name__contains='Spanish')

    context = {
        'courses': courses,
        'spanish_courses': spanish_courses,
    }

    return render(request, 'courses/courses.html', context)

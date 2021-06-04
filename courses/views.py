from django.shortcuts import render
from .models import Course

# Create your views here.
def all_courses(request):
    """shows all courses"""

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)

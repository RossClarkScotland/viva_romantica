from django.urls import path
from . import views

urlpatterns = [
    path('spanish', views.spanish_courses, name='spanish'),
    path('french/', views.french_courses, name='french'),
    path('italian/', views.italian_courses, name='italian'),
    path('portugese/', views.portugese_courses, name='portugese'),
    path('romanian/', views.romanian_courses, name='romanian'),
    path('<course_id>', views.course_details, name='course_details'),
]

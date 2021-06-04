from django.contrib import admin
from .models import Course, Language


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'description',
        'price',
        'sku',
    )

    ordering = ('image',)

class LanguageAdmin(admin.ModelAdmin):
     list_display = (
         'friendly_name',
         'name',
     )

admin.site.register(Course, CourseAdmin)
admin.site.register(Language, LanguageAdmin)

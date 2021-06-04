from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Course(models.Model):
    language = models.ForeignKey('Language', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField()

    def __str__(self):
        return self.name


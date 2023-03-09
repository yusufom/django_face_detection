from django.contrib import admin

# Register your models here.

from .views import Image

admin.site.register(Image)

from django.contrib import admin
from . models import *
# Register your models here.

class Institute_display(admin.ModelAdmin):
    list_display=['name','image']

admin.site.register(Institute,Institute_display)

from django.contrib import admin
from .models import image_model
# Register your models here.

@admin.register(image_model)
class image_admin(admin.ModelAdmin):
    list_display=['id','photo','date']
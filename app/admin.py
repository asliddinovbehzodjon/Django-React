from django.contrib import admin

# Register your models here.
from .models import Menu,Mahsulot
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']


@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    search_fields=['title','menu','desc','cost']
    list_display=['title','menu','cost']

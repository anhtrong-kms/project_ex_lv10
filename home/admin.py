from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'date']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','number', 'image', 'date']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
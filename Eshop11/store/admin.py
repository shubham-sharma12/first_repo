from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models import *

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

# class AdminCategory(admin.ModelAdmin):
#     list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','id']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order)
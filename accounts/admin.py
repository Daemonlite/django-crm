from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'date_created']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','description' ,'date_created']

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'date_created', 'status']





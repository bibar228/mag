from django.contrib import admin

# Register your models here.
from bizz.models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', "price"]

admin.site.register(Products, ProductsAdmin)
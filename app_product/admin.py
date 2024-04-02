from django.contrib import admin

from .models import Shop, Product, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Shop)

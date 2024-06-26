from django.contrib import admin
from .models import product
from .category import Category

from .customer import customer
# Register your models here.


class categoryInfo(admin.ModelAdmin):
    list_display = ["name"]


class productInfo(admin.ModelAdmin):
    list_display = ["name", "Category", "price"]


class signupdata(admin.ModelAdmin):
    list_display = ["email"]


admin.site.register(product, productInfo)
admin.site.register(Category, categoryInfo)
admin.site.register(customer, signupdata)
# admin.site.register(CartItem)

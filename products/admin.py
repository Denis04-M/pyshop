from django.contrib import admin
from .models import *


# class ProductAdmin(admin.ModelAdmin):  # try and remove this
#     list_display = ('name', 'price', 'stock')
#
#
# class OfferAdmin(admin.ModelAdmin):  # try and remove this
#     list_display = ['code', 'discount']


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)
admin.site.register(Customer)
admin.site.register(ItemsOrdered)
admin.site.register(Report)
admin.site.register(Chart)

from django.contrib import admin

from .models import Category, Item, Prescription, Rating, Coupon

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Prescription)
admin.site.register(Rating)
admin.site.register(Coupon)
from django.contrib import admin
from .models import Product, Offer,Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'admission_no', 'password')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)


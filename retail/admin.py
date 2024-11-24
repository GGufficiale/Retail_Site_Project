from django.contrib import admin
from retail.models import Contacts, Product, Factory, RetailNetwork, IP


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('city',)
    search_fields = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'price', 'manufactured_at')


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'debt', 'created_at')
    list_filter = ('contact',)
    search_fields = ('contact',)


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'debt', 'created_at', 'factory_supplier')
    list_filter = ('contact', 'factory_supplier')
    search_fields = ('contact', 'factory_supplier')


@admin.register(IP)
class IPAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'debt', 'created_at', 'factory_supplier', 'retail_network_supplier')
    list_filter = ('contact', 'factory_supplier', 'retail_network_supplier')
    search_fields = ('contact', 'factory_supplier', 'retail_network_supplier')

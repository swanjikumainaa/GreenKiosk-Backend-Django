# from django.contrib import admin

# # Register your models here.

# from .models import Shopping_cart

# class adding_to_cart(admin.ModelAdmin):
#     list_display=('','total_price','quantity')
    
# admin.site.register(Shopping_cart,adding_to_cart)   

from django.contrib import admin
from .models import Shopping_cart

class Shopping_cartAdmin(admin.ModelAdmin):
    list_display = ['customerName', 'get_products', 'user_id', 'total_price', 'quantity']

    def get_products(self, obj):
        return ', '.join([str(product) for product in obj.products.all()])

admin.site.register(Shopping_cart, Shopping_cartAdmin)



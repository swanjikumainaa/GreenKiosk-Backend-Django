from django.contrib import admin

# Register your models here.

from .models import Shopping_cart

class adding_to_cart(admin.ModelAdmin):
    list_display=('products','total_price','quantity')
    
admin.site.register(Shopping_cart,adding_to_cart)   
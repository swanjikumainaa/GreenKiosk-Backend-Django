from django.contrib import admin

# Register your models here.
from .models import Discounts

class DiscountsAdmin(admin.ModelAdmin):
    list_display=('product','code','percentage','minimum_purchase','expiry_date')
    
admin.site.register(Discounts,DiscountsAdmin) 




 
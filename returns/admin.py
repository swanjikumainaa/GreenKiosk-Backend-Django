from django.contrib import admin

# Register your models here.
from .models import Refunds

class RefundsAdmin(admin.ModelAdmin):
    list_display=('amount','reason','request_date')
    
admin.site.register(Refunds,RefundsAdmin)   





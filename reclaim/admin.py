from django.contrib import admin

# Register your models here.
from .models import Account_recovery

class Account_recoveryAdmin(admin.ModelAdmin):
    list_display=('username','email','user_id')
    
admin.site.register(Account_recovery,Account_recoveryAdmin) 



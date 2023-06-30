from django.contrib import admin

# Register your models here.


from .models import Search_engine

class Search_engineAdmin(admin.ModelAdmin):
    list_display=('search_query','results','timestamp')
    
admin.site.register(Search_engine,Search_engineAdmin) 

  
 
  
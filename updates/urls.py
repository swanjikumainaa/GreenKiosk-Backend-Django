from django.urls import path
from .views import add_notifications


urlpatterns =[
    path ("notifications/add",add_notifications,name = "notifications_add_view"),
]

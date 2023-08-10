from django.urls import path
from .views import upload_discount


urlpatterns =[
    path ("discounts/upload",upload_discount,name = "discounts_upload_view"),
]

from django.urls import path
from .views import register_vendor

urlpatterns =[
path ("vendors/registration",register_vendor,name = "vendor_registration_view"),
]

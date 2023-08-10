from django.urls import path
from .views import dispatch_shipment


urlpatterns =[
    path ("shipments/dispatch",dispatch_shipment,name = "shipment_dispatch_view"),
]

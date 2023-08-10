from django.urls import path
from .views import place_order


urlpatterns =[
    path ("orders/placement",place_order,name = "order_placement_view"),
]

from django.urls import path
from .views import place_order,orders_list,order_detail,edit_order_view


urlpatterns =[
    path ("orders/placement",place_order,name = "order_placement_view"),
    path ("orders/list",orders_list,name = "orders_list_view"),
    path ("orders/<int:id>/",order_detail,name = "order_detail_view"),
    path ("order/edit/<int:id>/",edit_order_view,name="order_edit_view"),  
]

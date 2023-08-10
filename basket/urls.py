from django.urls import path
from .views import add_cart


urlpatterns =[
    path ("shopping_cart/add",add_cart,name = "add_cart_view"),
]

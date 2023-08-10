from django.urls import path
from .views import make_payment


urlpatterns =[
    path ("payments/make",make_payment,name = "make_payment_view"),
]

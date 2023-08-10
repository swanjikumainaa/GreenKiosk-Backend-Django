from django.urls import path
from .views import request_recovery


urlpatterns =[
    path ("account_recovery/request",request_recovery,name = "account_recovery_view"),
]

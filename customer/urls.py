from django.urls import path
from .views import register_user


urlpatterns =[
path ("users/registration",register_user,name = "user_registration_view"),
]

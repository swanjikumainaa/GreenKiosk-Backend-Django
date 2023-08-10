from django.shortcuts import render
from .forms import UserRegistrationForm


# Create your views here.


def register_user(request):
    form = UserRegistrationForm()
    return render(request,"customer/user_registration.html",{"form":form})

from django.shortcuts import render

# Create your views here.
from .forms import VendorRegistrationForm


# Create your views here.


def register_vendor(request):
    form = VendorRegistrationForm()
    return render(request,"seller/vendor_registration.html",{"form":form})



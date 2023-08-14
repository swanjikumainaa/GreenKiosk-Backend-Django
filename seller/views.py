from django.shortcuts import render
from .models import Vendor
from django.shortcuts import redirect


# Create your views here.
from .forms import VendorRegistrationForm


# Create your views here.


def register_vendor(request):
    form = VendorRegistrationForm()
    return render(request,"seller/vendor_registration.html",{"form":form})

def vendors_list(request):
    vendors = Vendor.objects.all()
    return render(request,"seller/vendors_list.html",{"vendors":vendors})

def vendor_detail(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request,"seller/vendor_detail.html",{"vendor":vendor})

def edit_vendor_view(request, id):
    vendor = Vendor.objects.get(id=id)
    if request.method == "POST":
        form = VendorRegistrationForm(request.POST,instance=vendor)
        if form.is_valid():
            form.save()
            return redirect("vendor_detail_view", id=vendor.id)
    else:
        form = VendorRegistrationForm(instance=vendor)
        return render(request,"seller/edit_vendor.html",{"form":form})
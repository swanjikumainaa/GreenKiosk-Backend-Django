from django.shortcuts import render
from .forms import DiscountUploadForm


# Create your views here.


def upload_discount(request):
    form = DiscountUploadForm()
    return render(request,"offers/discount_upload.html",{"form":form})

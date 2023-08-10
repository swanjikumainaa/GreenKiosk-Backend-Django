from django.shortcuts import render
from .forms import ReviewUploadForm


# Create your views here.


def upload_review(request):
    form = ReviewUploadForm()
    return render(request,"feedback/review_upload.html",{"form":form})
from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product

# Create your views here.

def upload_product(request):
    if request.method == "POST":
        form = ProductUploadForm(request.POST,request.Files)
        if form.is_valid():
            form.save
    else:
        form = ProductUploadForm()        
   
    return render(request,"inventory/product_upload.html",{"form":form})


def products_list(request):
    products = Product.objects.all()

    return render(request,"inventory/products_list.html",{"products":products})

def product_detail(request, id):
    product = Product.objects.get(id=id)

    return render(request,"inventory/product_detail.html",{"product":product})
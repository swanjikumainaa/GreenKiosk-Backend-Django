from django.shortcuts import render
from .forms import CartAddForm


# Create your views here.


def add_cart(request):
    form = CartAddForm()
    return render(request,"basket/add_cart.html",{"form":form})

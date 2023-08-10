from django.shortcuts import render
from .forms import OrderPlacementForm


# Create your views here.


def place_order(request):
    form = OrderPlacementForm()
    return render(request,"purchases/order_placement.html",{"form":form})
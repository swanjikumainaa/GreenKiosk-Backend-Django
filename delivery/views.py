from django.shortcuts import render
from .forms import DispatchShipmentForm


# Create your views here.


def dispatch_shipment(request):
    form = DispatchShipmentForm()
    return render(request,"delivery/shipment_dispatchment.html",{"form":form})
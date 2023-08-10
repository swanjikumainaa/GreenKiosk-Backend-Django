from django.shortcuts import render
from .forms import MakePaymentForm


# Create your views here.


def make_payment(request):
    form = MakePaymentForm()
    return render(request,"transactions/make_payment.html",{"form":form})


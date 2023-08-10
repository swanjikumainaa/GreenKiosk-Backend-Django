from django.shortcuts import render
from .forms import RecoverAccountForm


# Create your views here.


def request_recovery(request):
    form = RecoverAccountForm()
    return render(request,"reclaim/recovery_account.html",{"form":form})

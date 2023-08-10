from django.shortcuts import render
from .forms import NotificationsAddForm


# Create your views here.


def add_notifications(request):
    form = NotificationsAddForm()
    return render(request,"updates/notifications_addition.html",{"form":form})

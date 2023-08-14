from django.shortcuts import render
from .forms import OrderPlacementForm
from .models import Order
from django.shortcuts import redirect

# Create your views here.


def place_order(request):
    form = OrderPlacementForm()
    return render(request,"purchases/order_placement.html",{"form":form})

def orders_list(request):
    orders = Order.objects.all()
    return render(request,"purchases/orders_list.html",{"orders":orders})

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request,"purchases/order_detail.html",{"order":order})

def edit_order_view(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderPlacementForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_detail_view", id=order.id)
    else:
        form =OrderPlacementForm(instance=order)
        return render(request,"purchases/edit_order.html",{"form":form})
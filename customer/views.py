from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import User
from django.shortcuts import redirect



# Create your views here.


def register_user(request):
    form = UserRegistrationForm()
    return render(request,"customer/user_registration.html",{"form":form})

def users_list(request):
    users = User.objects.all()
    return render(request,"customer/users_list.html",{"users":users})

def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request,"customer/user_detail.html",{"user":user})

def edit_user_view(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_detail_view", id=user.id)
    else:
        form = UserRegistrationForm(instance=user)
        return render(request,"customer/edit_user.html",{"form":form})

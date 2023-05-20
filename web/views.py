from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.decorators import login_required
import json
from .models import Products

# from .forms import LoginForm, RegistrationForm

def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)

def shop(request):
    products = Products.objects.all()

    # Get the current sort order
    sort_order = request.GET.get("sort_by", "")

    # Sort the products by the current sort order
    if sort_order == "price_low_high":
        products = products.order_by("price")
    elif sort_order == "price_high_low":
        products = products.order_by("-price")


    context = {
        "is_shop": True,
        "products": products,
    }
    return render(request, "web/shop.html", context)

def product_details(request,id):

    product=Products.objects.get(id=id)
    context={"is_product":True,'product':product}
    return render (request,"web/product-details.html",context)

def register_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:register')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:register')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/register.html")

def login_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:register')
    return render(request,"web/login.html")

from home.models import new_models, product
from home.models import register_id
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from . import admin
from .forms import CreateForm


# Create your views here.
def home(request):
    products=product.objects.all()
    update=new_models.objects.all()

    return render(request,'index.html',{'products':products,'update':update})

@login_required(login_url='login')
def product_detail(request):
    products=product.objects.all()
    update=new_models.objects.all()
    return render(request,'product-detail.html',{'products':products,'update':update})

def product_list(request):
    products=product.objects.all()
    update=new_models.objects.all()
    return render(request,'product-list.html',{'products':products,'update':update})

def contact(request):
    products=product.objects.all()
    update=new_models.objects.all()
    return render(request,'contact.html',{'products':products,"update":update})


@login_required(login_url='login')
def wishlist(request):
    products=product.objects.all()
    update=new_models.objects.all()
    return render(request,'wishlist.html',{'products':products,"update":update})

@login_required(login_url='login')
def cart(request):
    products=product.objects.all()
    update=new_models.objects.all()
    return render(request,'cart.html',{'products':products,"update":update})

@login_required(login_url='login')
def checkout(request):
    products=product.objects.all()
    update=new_models.objects.all()
    return render(request,'checkout.html',{'products':products,"update":update})

def register_id(request):
    form=CreateForm()
    if request.method == 'POST':
        form=CreateForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'You Have Successely Registered : ' +  user)
            return redirect("login")
       
    content={'form':form}
    return render(request,'register.html',content)

def login_id(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,"User Is Not Created ")

    content={}
    return render(request,'login.html',content)


def logout_user(request):
    logout(request)
    return redirect('login')
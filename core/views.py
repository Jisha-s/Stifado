from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):

    return render(request,"index.html")

def login(request):
    return render(request,"login.html") 

def signup(request):
    return render(request,"signup.html") 

def cart(request):
    return render(request,"cart.html") 

def product_list(request):
    return render(request,"product_list.html") 

def checkout(request):
   return render(request,'checkout.html')

def authViews(request):
    if request.method == "POST":
     form = UserCreationForm(request.post or None)
     if form.is_valid():
         form.save()
    else:
     form = UserCreationForm()
    return render(request,"registration/signup.html",{"form":form}) 

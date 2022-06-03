from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return render(request, "photoapp/index.html")

def sign_up(request):
    return render(request, 'auth/sign_up.html')

def login(request):
    return render(request, 'auth/login.html')

def profile(request):
    return render(request, 'photoapp/profile.html')

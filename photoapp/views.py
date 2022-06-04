from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.http import HttpResponse 
from .models import Profile,Image,Comment,Like

# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    posts = Image.objects.all()


    context = {'profiles': profiles, 'posts': posts}
    return render(request, "photoapp/index.html", context)

def sign_up(request):
    return render(request, 'auth/sign_up.html')

def login(request):
    return render(request, 'auth/login.html')

def profile(request):
    return render(request, 'photoapp/profile.html')

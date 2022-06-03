from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse ("Hello, world. You're at the instaclone index page.")

def sign_up(request):
    return HttpResponse ("This is the registration page")

def login(request):
    return HttpResponse ("This is login page")

def profile(request):
    return HttpResponse ("This is user profile page") 

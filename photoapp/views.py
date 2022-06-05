from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.http import HttpResponse 
from django.contrib import messages 
from .models import Profile,Image,Comment,Like
from .forms import UpdateProfileForm,NewPostForm,CommentForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def index(request):
    posts = Image.objects.all()


    context = {'posts': posts}
    return render(request, 'photoapp/index.html', context)


def create_post(request):
    current_user = request.user 
    profile = Profile.objects.get(user = request.user.id)
    title = 'New Post'

    form = NewPostForm(request.POST, request.FILES)  
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = profile
            post.save()
            return redirect('profile', current_user.id)
        else:
            form = NewPostForm()

    context = {'form': form, 'title':title}
    return render(request, 'photoapp/create_post.html', context)



def profile(request, id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.filter(user=id) 
    images = Image.objects.filter(user=id)


    context = {'user': user, 'images': images, 'profile': profile} 
    return render(request, 'photoapp/profile.html', context)



def update_profile(request):
    context = {}
    return render(request, 'photoapp/update_profile.html', context)





def sign_up(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user) 
            return redirect('index')
        
        else:
            messages.error(request, 'Registration failed!!')

    context = {'form': form}
    return render(request, 'auth/sign_up.html', context)




def login(request):
    # page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User do not exist')
            
        user = authenticate(request, username=username, password=password) 


        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Wrong username or password')

    context = {}
    return render(request, 'auth/login.html', context)



def logout(request):
    logout(request)
    return redirect('index')



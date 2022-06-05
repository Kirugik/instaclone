from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.http import HttpResponse 
from .models import Profile,Image,Comment,Like
from .forms import UpdateProfileForm,NewPostForm,CommentForm

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
    return render(request, 'auth/sign_up.html')

def login(request):
    return render(request, 'auth/login.html')



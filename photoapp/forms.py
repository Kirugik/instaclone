from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from .models import Profile, Image, Comment 


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['user', 'image', 'image_caption']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['body']

class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['email', 'full_name', 'username', 'password1', 'password2'] 

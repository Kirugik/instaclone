from django import forms
from .models import Profile, Image, Comment 


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'image_caption']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['body']
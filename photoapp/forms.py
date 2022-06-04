from django import forms
from .models import Profile, Image, Comment 


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'image_caption'] 
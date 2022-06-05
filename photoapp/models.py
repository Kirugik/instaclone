from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    email = models.EmailField(null=True, unique=True)
    full_name = models.CharField(max_length =100, null=True)
    username = models.CharField(max_length =50, null=True, unique=True) 
    password = models.CharField(max_length=50, null=True) 
    profile_photo = models.ImageField(upload_to='profile_images/', blank=True) 
    bio = models.CharField(max_length=200, blank=True) 
    
    USERNAME_FIELD = 'username'

    def __str__(self): 
        return self.username  



class Image(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='posts') 
    image = models.ImageField(upload_to='posts/') 
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField(max_length=200, null=True, blank=True) 
    posted = models.DateTimeField(auto_now_add=True) 
    # author = models.ForeignKey(User, on_delete=models.CASCADE) 
    likes = models.ForeignKey('Like', on_delete=models.CASCADE,null=True, blank=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ['-posted']  
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save() 

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls, id, caption):
        new_caption = cls.objects.filter(pk=id).update(image_caption=caption)
        return new_caption 
    


class Comment(models.Model):
    body = models.TextField(max_length=100) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    image_id = models.ForeignKey(Image,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)  
    count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-posted_on']   
        
    def __str__(self): 
        return self.body   



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE) 


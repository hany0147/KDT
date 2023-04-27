from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_post')
    select1_content = models.TextField()
    img1 = models.ImageField(blank=True, upload_to='images1/')
    img1_thumbnail = ImageSpecField(source='img1',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 100})
    
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_post')
    select2_content = models.TextField()
    img2 = models.ImageField(blank=True, upload_to='images2/')
    img2_thumbnail = ImageSpecField(source='img2',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 100})



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

# class PostImage(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     img1 = models.ImageField(blank=True, upload_to='images1/')
#     img2 = models.ImageField(blank=True, upload_to='images2/')

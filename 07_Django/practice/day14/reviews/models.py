from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    image_thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(300, 300)],
        options={'quality': 100}
    )
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review ,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
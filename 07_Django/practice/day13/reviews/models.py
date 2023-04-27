from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie = models.CharField(max_length=80)
    image = models.ImageField(blank=True, upload_to='imgs/')
    image_thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(500, 500)],
        options={'quality': 100}
    )

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()

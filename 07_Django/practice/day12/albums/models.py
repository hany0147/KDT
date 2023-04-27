from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Album(models.Model):
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='imgs/')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        options={'quality': 80}
    )
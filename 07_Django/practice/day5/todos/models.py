from django.db import models

# Create your models here.
class Todo(models.Model):
    # 부모 클래스를 모두 상속
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    category = models.CharField(max_length=20, null=True)
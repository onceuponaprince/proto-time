from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='like_set')
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    published = models.DateTimeField(auto_now=True)

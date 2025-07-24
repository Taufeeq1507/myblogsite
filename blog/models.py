from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    is_editorschoice = models.BooleanField(default=False)
    summary = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='blog_images/', default='blog_images/logo.png')

    def __str__(self):
        return self.title
        
    
# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     author = models.CharField(max_length=100)
#     content = models.TextField()
#     date_created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f'Comment by {self.author} on {self.post.title}'

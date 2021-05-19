from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Picture', upload_to='post/%Y/%m/%d')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('Content:detail_post', args=[self.id])


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments_author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments_post', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)





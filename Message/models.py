from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message_title = models.CharField(max_length=100)
    message_content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
from django.shortcuts import render
from Content.models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'Content/index.html', {'posts': posts})
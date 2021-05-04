from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from Content.paginator import pag
from Content.models import Post
from Content.forms import AddPostForm

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'Content/index.html', {'posts': posts})


@login_required
def add_post(request):
    if request.method == 'POST':
        data = request.POST
        form = AddPostForm(data, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('Content:index')
    else:
        form = AddPostForm()
        return render(request, 'Content/add_post.html', {'form': form})


class DetailPost(View):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        return render(request, 'Content/detail_post.html', {'post': post})





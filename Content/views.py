from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
            new_post.user = request.user
            new_post.save()
            return redirect('Content:index')
    else:
        form = AddPostForm()
        return render(request, 'Content/add_post.html', {'form': form})
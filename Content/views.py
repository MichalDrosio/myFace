from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from Content.models import Post, Comment
from Content.forms import AddPostForm, AddCommentForm

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


@login_required
def detail_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post)
    data = request.POST
    if request.method == 'POST':
        form = AddCommentForm(data, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.post = post
            new_form.save()
            messages.success(request, 'Added comment ')
        else:
            messages.error(request, 'There was an error adding your comment')
        return HttpResponseRedirect(reverse('Content:detail_post', args=[post_id]))
    else:
        form = AddCommentForm()
    return render(request, 'Content/detail_post.html', {'post': post, 'form': form, 'comments': comments})


@login_required
def delete_post(request, post_id):
    posts = Post.objects.filter(author=request.user)
    post = posts.get(pk=post_id)
    post.delete()
    return redirect('/')





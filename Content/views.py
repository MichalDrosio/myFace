from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from Content.paginator import pag
from Content.models import Post, Comment
from Content.forms import AddPostForm, AddCommentForm
from django.db.models import Q
# Create your views here.


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(date_added__icontains=search_query) |Q(post_title__icontains=search_query))
    else:
        posts = Post.objects.all()
        paginator = Paginator(posts, 3)
        page = request.GET.get('page', 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    return render(request, 'Content/index.html', {'posts': posts, 'page': posts})


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
            if new_form.save():
                messages.success(request, 'Comment has been added')
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


def delete_comment(request, post_id, comment_id):
    comments = Comment.objects.filter(author=request.user)
    comment = get_object_or_404(comments, pk=comment_id)
    if comment.delete():
        messages.success(request, f"Comment {comment.author}  has been deleted")
    else:
        messages.error(request, "You cannot delete this post")
    return redirect('Content:detail_post', post_id)





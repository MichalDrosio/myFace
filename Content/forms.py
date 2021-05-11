from Content.models import Post, Comment
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
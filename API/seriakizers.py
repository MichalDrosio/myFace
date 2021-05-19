from django.contrib.auth.models import User
from rest_framework import serializers
from Content.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'date_added')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    comments = CommentsSerializer()

    class Meta:
        model = Post
        fields = ('id', 'author', 'post_title', 'text', 'date_added', 'comments')




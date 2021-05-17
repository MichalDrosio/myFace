from django.contrib import admin
from Content.models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'post_title', 'text', 'date_added', 'image']


admin.site.register(Comment)
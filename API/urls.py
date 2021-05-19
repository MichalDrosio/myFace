from django.urls import path

from API.views import PostListView, PostDetailView

app_name = 'API'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list_api'),
    path('posts/<pk>/', PostDetailView.as_view(), name='post_detail_api')
]
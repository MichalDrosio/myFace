from django.urls import path
from . import views

app_name = 'Content'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-post/', views.add_post, name='add_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post-detail/<int:post_id>/', views.detail_post, name='detail_post'),
]
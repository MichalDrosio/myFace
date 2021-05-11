from django.urls import path, include
from Account.views import login_user, register_user, user_logout, user_detail

app_name = 'Account'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', user_logout, name='logout'),
    path('user-detail/', user_detail, name='user_detail'),


]
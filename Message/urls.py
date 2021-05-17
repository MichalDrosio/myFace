from django.urls import path
from . import views

app_name = 'Message'

urlpatterns = [
    path('', views.list_messages, name='list_messages'),
    path('create-message/', views.create_message, name='create_message'),
    path('mess_list/<int:user_id>/', views.messages_users, name='messages_users'),
    path('index/', views.index_message, name='index_message'),
    path('<str:room_name>/', views.room, name='room'),

]
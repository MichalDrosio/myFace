from django.urls import path
from . import views

app_name = 'Message'

urlpatterns = [
    path('', views.list_messages, name='list_messages'),
    path('create-message/', views.create_message, name='create_message'),

]
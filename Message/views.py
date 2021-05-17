from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from Message.models import Message
from Message.forms import CreateMessageForm
from django.contrib import messages


@login_required
def list_messages(request):
    messages_receiver = Message.objects.filter(sender=request.user)
    receiver_message = []
    for i in messages_receiver:
        if i.receiver not in receiver_message:
            receiver_message.append(i)
    messages_sender = Message.objects.filter(receiver=request.user)
    sender_message = []
    for j in messages_sender:
        if j.sender not in sender_message:
            sender_message.append(j)
    return render(request, 'Message/messages.html',
                  {'messages_receiver': messages_receiver, 'messages_sender': messages_sender,
                   'receiver_message': receiver_message, 'sender_message': sender_message})


@login_required
def messages_users(request, user_id):
    user_mes = Message.objects.get(id=user_id)
    return render(request, 'Message/list_messages.html')


@login_required
def create_message(request):
    if request.method == 'POST':
        message_form = CreateMessageForm(request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.sender = request.user
            new_message.save()
            return render(request, 'Message/messages.html')
    else:
        message_form = CreateMessageForm()
    return render(request, 'Message/send_box.html', {'message_form': message_form})


def index_message(request):
    return render(request, 'Message/index_message.html')


def room(request, room_name):
    return render(request, 'Message/room.html', {"room_name": room_name})
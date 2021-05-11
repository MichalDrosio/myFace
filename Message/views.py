from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Message.models import Message
from Message.forms import CreateMessageForm


@login_required
def list_messages(request):
    messages_receiver = Message.objects.filter(sender=request.user)
    messages_sender = Message.objects.filter(receiver=request.user)
    return render(request, 'Message/messages.html',
                  {'messages_receiver': messages_receiver, 'messages_sender': messages_sender})


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
from django import forms
from django.contrib.auth.models import User

from Message.models import Message


class ChoseReceiver(forms.Select):
    class Meta:
        model = User
        fields = ('username',)


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('sender', 'created')
        widgets = {'receiver': ChoseReceiver}


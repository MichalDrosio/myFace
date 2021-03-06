from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from Account.forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Account:user_detail')
    else:
        form = LoginForm()
    return render(request, 'Account/login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Thank you for joining, now you can log in')
            return redirect('Content:index',)
    else:
        form = UserRegistrationForm()
    return render(request, 'Account/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'Content/index.html')


@login_required
def user_detail(request):
    # messages_sender = Message.objects.filtre(sender=request.user)
    # messages_receiver = Message.objects.filtre(receiver=request.user)
    return render(request, 'Account/user_detail.html')
                  # {'messages_receiver': messages_receiver, 'messages_sender': messages_sender})



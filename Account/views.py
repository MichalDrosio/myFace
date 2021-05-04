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
                    return render(request, 'Content/index.html')
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
            return render(request, 'Content/index.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'Account/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'Content/index.html')



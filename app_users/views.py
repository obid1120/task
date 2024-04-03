from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm(request.POST)
        return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

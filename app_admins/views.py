from django.shortcuts import render

from .models import AdminsUser


def register(request):
    if request.POST == "POST":
        pass
    else:
        form = AdminsUser(request.POST)
        return render(request, 'registration/register.html', {"form": form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            login(request, user)
            messages.success(request, f"Создан аккаунт {username}!")
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

from django.shortcuts import render, redirect #render — показывает HTML-страницу пользователю. redirect — перенаправляет пользователя на другую страницу после действия.
# Create your views here.
from .models import UserProfile



def index(request):
    return render(request, template_name="index.html")

def register(request):
    return render(request, template_name="register.html")

def users(request):
    return render(request, template_name="users.html")

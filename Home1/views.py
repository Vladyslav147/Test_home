from django.shortcuts import render, redirect #render — показывает HTML-страницу пользователю. redirect — перенаправляет пользователя на другую страницу после действия.
# Create your views here.
from .models import UserProfile



def index(request):
    return render(request, template_name="index.html")

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        user_email = request.POST.get('email')

        UserProfile.objects.create(name = user_name, phone = user_phone, email = user_email)
        return redirect('index')
    return render(request, template_name="register.html")


def users(request):
    all_users = UserProfile.objects.all()
    contex = {
        'users': all_users
    }
    return render(request, template_name="users.html", context=contex)







"""
def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone') #.get - пишется для того что бы есле не найдет такого поля просто вывело none, Можно и без .get просто при случае когда данных не найдет выведет ошыбку (но только не в () а в [])

        UserProfile.objects.create( # С помощью objects можно: создавать новые записи (create), получать все записи (all), фильтровать записи (filter), …и многое другое.
            name = user_name,
            phone = user_phone
        )
        return redirect('index')

    return render(request, template_name="register.html")
"""
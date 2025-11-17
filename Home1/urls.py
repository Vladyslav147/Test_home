from django.urls import path
from Home1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("users/", views.users, name="users"),
]

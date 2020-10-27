from django.urls import path, re_path

from . import views

urlpatterns = [
    path('registration/',
         views.registration, name="registration"),
    path('home/',
         views.home, name="home"),
    path('login/',
         views.login, name="login"),
    path('', views.home, name="home"),
]

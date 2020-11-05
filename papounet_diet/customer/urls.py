from django.urls import path, re_path

from . import views

app_name = "customer"
urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.login, name="login"),
]

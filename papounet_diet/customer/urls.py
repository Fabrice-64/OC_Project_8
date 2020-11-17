from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "customer"
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', auth_views.LogoutView.as_view, name="logout"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
]

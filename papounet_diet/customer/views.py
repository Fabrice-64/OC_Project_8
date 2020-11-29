from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm


def user_login(request):
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
                    return render(request, "customer/home.html")
                else:
                    info = "Votre compte est désactivé"
                    return render(request, "customer/failed_login.html", {'info': info, 'next_step': "create_account"})
            else:
                info = "Vos identifiants sont incorrects"
                return render(request, "customer/failed_login.html", {'info': info, 'next_step': "log_in_again"})
    else:
        form = LoginForm()

    return render(request, "customer/login.html", {'form': form})

def user_logout(request):
    logout(request)
    return render(request, "customer/home.html")


def home(request):
    return render(request, "customer/home.html")

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'customer/home.html')
    else:
        user_form = UserRegistrationForm()

    return render(request, "customer/register.html", {'user_form': user_form})

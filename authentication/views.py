from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import logout as dj_logout, authenticate, login as dj_login
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User


# LOGIN VIEW ENDPOINT
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.errors)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('email')

            messages.success(
                request, f'Account Succesfully Created for {username}')
            return redirect('login')

    context = {'form': form}
    print('here')
    return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            dj_login(request, user)

            return redirect('posts')

        else:
            print(user)
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')


def logout(request):
    print('Hello')
    dj_logout(request)
    return redirect('login')

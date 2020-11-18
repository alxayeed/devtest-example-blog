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

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('email')

            messages.success(
                request, f'Account Succesfully Created for {username}. Please log in')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            dj_login(request, user)

            return redirect('posts')

        else:
            messages.info(
                request, 'Oops! There is a problem with your email or password.\
                    Please register or try again')

    return render(request, 'login.html')


def logout(request):
    dj_logout(request)
    return redirect('login')

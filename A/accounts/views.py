from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from .forms import UserLoginForm,UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'you login successfully','success')
                return redirect('blog:all_articles')
            else:
                messages.error(request,'wrong username or password','danger')
    else:
        form = UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request,'you register successfully','success')
            return redirect('accounts:user_login')
    else:
        form = UserRegisterForm()
    return render(request,'accounts/register.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'you are log out')
    return redirect('blog:all_articles')

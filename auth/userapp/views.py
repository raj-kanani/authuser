from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import registerform, editform, editadminform
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def register(request):
    if request.method == 'POST':
        fm = registerform(request.POST)
        if fm.is_valid():
            messages.success(request, 'account created')
            fm.save()
            return HttpResponseRedirect('/loggin/')
    else:
        fm = registerform()
    return render(request, 'register.html', {'form': fm})


def loggin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login user  !!!!!')
                    return HttpResponseRedirect('/index/')

        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/index/')


def loggout(request):
    logout(request)
    return HttpResponseRedirect('/loggin/')


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = editadminform(request.POST, instance=request.user)

            else:
                 fm = editform(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'data update')
        else:
            if request.user.is_superuser == True:
                fm = editadminform(instance=request.user)
            else:
                fm = editform(instance=request.user)
        return render(request, 'index.html', {'name': request.user.username, 'form': fm})
    else:
        return HttpResponseRedirect('/loggin/')


# simple index without user data display
# def index(request):
#     if request.user.is_authenticated:
#         fm = UserChangeForm(instance=request.user)
#         return render(request, 'index.html', {'name': request.user, 'form': fm})
#     else:
#         return HttpResponseRedirect('/loggin/')

# change pwd with old passoword
def change_pwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = PasswordChangeForm(user=request.user, data=request.POST)
            if f.is_valid():
                f.save()
                update_session_auth_hash(request, f.user)
                messages.success(request, 'password change success.')
                return HttpResponseRedirect('/index/')
        else:
            f = PasswordChangeForm(user=request.user)
        return render(request, 'password.html', {'form': f})
    else:
        return HttpResponseRedirect('/loggin/')


# change pwd without old pwd
def change_pwd1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = SetPasswordForm(user=request.user, data=request.POST)
            if f.is_valid():
                f.save()
                update_session_auth_hash(request, f.user)
                messages.success(request, 'password change success.')
                return HttpResponseRedirect('/index/')
        else:
            f = SetPasswordForm(user=request.user)
        return render(request, 'password1.html', {'form': f})
    else:
        return HttpResponseRedirect('/loggin/')

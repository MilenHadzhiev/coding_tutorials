from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm
from accounts.models import UserProfile


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm,
        }
        return render(request, 'accounts/register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()
            login(request, user)
            return redirect('current user profile')
        context = {
            'form': form,
        }
        return render(request, 'accounts/register.html', context)


def profile_user(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'user_profile.html', context)


def profile_user_edit(request):
    pass


def logout_user(request):
    logout(request)
    return redirect('homepage')

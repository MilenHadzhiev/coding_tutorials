from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, UserProfileEditForm
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
    tutorials = user.tutorial_set.all()
    notes = user.note_set.all()
    context = {
        'user': user,
        'tutorials': tutorials,
        'has_edit_link': pk is None,
        'notes': notes,
    }
    return render(request, 'accounts/user_profile.html', context)


@login_required
def profile_user_edit(request):
    user = request.user
    if request.method == 'GET':
        initial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'profile_picture': user.userprofile.profile_picture,
            'github': user.userprofile.github,
            'address': user.userprofile.address,
            'personal_website': user.userprofile.personal_website,
            'about': user.userprofile.about,
        }
        context = {
            'form': UserProfileEditForm(initial=initial),
            'user': user,
        }
        return render(request, 'accounts/user_profile_edit.html', context)
    else:
        form = UserProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('current user profile')
        context = {
            'form': form,
        }
        return render(request=request, template_name='accounts/user_profile_edit.html', context=context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('homepage')

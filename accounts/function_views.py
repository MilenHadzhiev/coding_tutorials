from django.contrib.auth import login
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
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
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


@login_required
def profile_user(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    tutorials = user.tutorial_set.all()
    notes = user.note_set.all()
    context = {
        'current_user': user,
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
            user = form.save()
            user.userprofile.profile_picture = form.cleaned_data['profile_picture']
            user.userprofile.github = form.cleaned_data['github']
            user.userprofile.address = form.cleaned_data['address']
            user.userprofile.personal_website = form.cleaned_data['personal_website']
            user.userprofile.about = form.cleaned_data['about']
            user.save()
            user.userprofile.save()
            return redirect('current user profile')
        context = {
            'form': form,
        }
        return render(request=request, template_name='accounts/user_profile_edit.html', context=context)

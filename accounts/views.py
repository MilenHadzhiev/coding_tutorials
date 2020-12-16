from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import RegisterForm, UserProfileEditForm
from accounts.models import UserProfile


class RegisterUser(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('current user profile')

    def form_valid(self, form):
        self.object = form.save()
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.save()
        profile = UserProfile(
            user=self.object,
        )
        profile.save()

        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)

        login(self.request, user)
        return valid


class ProfileUser(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user_profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        context['current_user'] = user
        context['tutorials'] = user.tutorial_set.all()
        context['notes'] = user.note_set.all()
        context['has_edit_link'] = pk is None
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)


class ProfileUserEdit(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user_profile_edit.html'
    form_class = UserProfileEditForm
    success_url = reverse_lazy('current user profile')
    model = User

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        initial['profile_picture'] = user.userprofile.profile_picture
        initial['github'] = user.userprofile.github
        initial['address'] = user.userprofile.address
        initial['personal_website'] = user.userprofile.personal_website
        initial['about'] = user.userprofile.about
        return initial

    def form_valid(self, form):
        self.object = form.save()
        self.object.userprofile.profile_picture = form.cleaned_data['profile_picture']
        self.object.userprofile.github = form.cleaned_data['github']
        self.object.userprofile.address = form.cleaned_data['address']
        self.object.userprofile.personal_website = form.cleaned_data['personal_website']
        self.object.userprofile.about = form.cleaned_data['about']
        self.object.save()
        self.object.userprofile.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)


@login_required
def logout_user(request):
    logout(request)
    return redirect('homepage')

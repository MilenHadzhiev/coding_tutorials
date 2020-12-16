from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from tutorials.forms import TutorialCreateForm
from tutorials.models import Tutorial


class TutorialCreate(LoginRequiredMixin, CreateView):
    form_class = TutorialCreateForm
    template_name = 'tutorials/create_tutorial.html'
    success_url = reverse_lazy('current user tutorials')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class TutorialsList(ListView):
    template_name = 'tutorials/tutorials_list.html'

    def get_queryset(self):
        self.queryset = Tutorial.objects.all()
        return self.queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutorials'] = self.get_queryset()
        context['is_user_tutorials_page'] = False
        return context


class TutorialsUser(LoginRequiredMixin, ListView):
    template_name = 'tutorials/tutorials_list.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        self.queryset = user.tutorial_set.all()
        return self.queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        context['user'] = user
        context['tutorials'] = self.get_queryset()
        context['has_create_link'] = pk is None
        context['is_user_tutorials_page'] = True
        return context


class TutorialPage(LoginRequiredMixin, DetailView):
    template_name = 'tutorials/tutorial_page.html'
    model = Tutorial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['tutorial'] = Tutorial.objects.get(pk=pk)
        context['can_change'] = self.request.user == context['tutorial'].user
        return context


class TutorialEdit(LoginRequiredMixin, UpdateView):
    template_name = 'tutorials/tutorial_edit.html'
    model = Tutorial
    form_class = TutorialCreateForm

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        if request.user != Tutorial.objects.get(pk=pk).user:
            return render(request, 'permission_denied.html')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy(
            'view tutorial page',
            kwargs={'pk': pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['tutorial'] = Tutorial.objects.get(pk=pk)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class TutorialDelete(LoginRequiredMixin, DeleteView):
    template_name = 'tutorials/tutorial_delete.html'
    model = Tutorial
    success_url = reverse_lazy('current user tutorials')

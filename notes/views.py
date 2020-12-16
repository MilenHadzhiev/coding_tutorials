from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from notes.forms import NoteCreateForm
from notes.models import Note
from tutorials.models import Tutorial


class NoteCreate(LoginRequiredMixin, CreateView):
    template_name = 'notes/note_create.html'
    form_class = NoteCreateForm

    def get_initial(self):
        pk = self.kwargs.get('pk')
        if pk is not None:
            tutorial = Tutorial.objects.get(pk=pk)
            return {'title': tutorial.tutorial_name}
        return super().get_initial()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.object.id
        return reverse_lazy('current note', kwargs={'pk': pk})


class NotesList(LoginRequiredMixin, ListView):
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        self.queryset = self.request.user.note_set.all()
        return self.queryset


class NotePage(LoginRequiredMixin, DetailView):
    template_name = 'notes/note_page.html'
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['note'] = Note.objects.get(pk=pk)
        return context


class NoteEdit(LoginRequiredMixin, UpdateView):
    template_name = 'notes/note_edit.html'
    model = Note
    form_class = NoteCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['note'] = Note.objects.get(pk=pk)
        return context

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('current note', kwargs={'pk': pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class NoteDelete(LoginRequiredMixin, DeleteView):
    template_name = 'notes/note_delete.html'
    model = Note
    success_url = reverse_lazy('my notes')

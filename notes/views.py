from django.shortcuts import render

from notes.forms import NoteCreateForm
from notes.models import Note
from tutorials.models import Tutorial


def note_create_post_persist(request):
    form = NoteCreateForm(request.POST)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        return note_page(request, pk=note.id)
    context = {
        'form': form,
    }
    return render(request, 'notes/note_create.html', context)


def note_create(request, pk=None):
    if pk is None:
        if request.method == 'GET':
            context = {
                'form': NoteCreateForm,
            }
            return render(request, 'notes/note_create.html', context)
        else:
            return note_create_post_persist(request)
    else:
        tutorial = Tutorial.objects.get(pk=pk)
        initial = {
            'title': tutorial.tutorial_name,
        }
        if request.method == 'GET':
            context = {
                'form': NoteCreateForm(initial=initial),
            }
            return render(request, 'notes/note_create.html', context)
        else:
            return note_create_post_persist(request)


def all_user_notes(request):
    user = request.user
    notes = user.note_set.all()
    notes_count = notes.count()
    context = {
        'user': user,
        'notes': notes,
        'notes_count': notes_count,
    }
    return render(request, 'notes/notes_list.html', context)


def note_page(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'notes/note_page.html', context)


def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        initial = {
            'title': note.title,
            'description': note.description,
        }
        context = {
            'note': note,
            'form': NoteCreateForm(initial=initial)
        }
        return render(request, 'notes/note_edit.html', context)
    else:
        form = NoteCreateForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return note_page(request, pk)
        context = {
            'form': form,
        }
        return render(request, 'notes/note_edit.html', context)


def note_delete(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'note': note,
        }
        return render(request, 'notes/note_delete.html', context)
    note.delete()
    return all_user_notes(request)

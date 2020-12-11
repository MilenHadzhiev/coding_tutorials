from django import forms

from notes.models import Note


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('user',)

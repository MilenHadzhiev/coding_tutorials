from django import forms

from tutorials.models import Tutorial


class TutorialCreateForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        exclude = ('user',)

from django import forms

from tutorials.models import Tutorial


class TutorialCreateForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        exclude = ('user',)

    # def clean(self):
    #     url = self.cleaned_data.get('url')
    #     tutorial_file = self.cleaned_data.get('tutorial_file')
    #     if not url and not tutorial_file:
    #         raise forms.ValidationError(
    #             'You must add either a link to the tutorial or a video file'
    #         )
    #
    #     return self.cleaned_data

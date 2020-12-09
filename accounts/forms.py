from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile
from core.BootstrapFormMixin import BootstrapFormMixin
from core.TextAreaAutoGrowMixin import TextAreaAutoGrowMixin


class RegisterForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class UserProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].required = False
        self.fields['github'].required = False
        self.fields['address'].required = False
        self.fields['date_of_birth'].required = False
        self.fields['personal_website'].required = False
        self.fields['about'].required = False

    class Meta:
        model = UserProfile
        exclude = ('user',)

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)

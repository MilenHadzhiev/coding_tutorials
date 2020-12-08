from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.BootstrapFormMixin import BootstrapFormMixin


class RegisterForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)


# class UserProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

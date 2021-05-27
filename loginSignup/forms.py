from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def verify_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']
            if password == confirm_password:
                return confirm_password

        raise forms.ValidationError('Passwords do not match.')

    def verify_unique_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$<', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')


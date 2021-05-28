from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    firstName = forms.CharField(label="firstName", max_length=30, widget=forms.TextInput (attrs={'placeholder': 'First Name', 'class': 'formEntry'}))
    lastName = forms.CharField(label="lastName", max_length=30, widget= forms.TextInput (attrs={'placeholder': 'Last Name', 'class': 'formEntry'}))
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput (attrs={'placeholder': 'Username', 'class': 'formEntry'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput (attrs={'placeholder': 'Email', 'class': 'formEntry'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput (attrs={'placeholder': 'Password', 'class': 'formEntry'}))
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput (attrs={'placeholder': 'Confirm Password', 'class': 'formEntry'}))


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

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
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            return username
        else:
            raise forms.ValidationError('Username is already taken.')


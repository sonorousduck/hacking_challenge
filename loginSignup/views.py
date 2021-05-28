from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, 'loginSignup/signinScreen.html')



def signUp(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.cleaned_data['username']).exists():
                if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                    print(form.verify_password)
                    user = User.objects.create_user(
                            username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                            email=form.cleaned_data['email']
                            )
                    user.save()
                    return HttpResponseRedirect('../..')
                else:
                    messages.error(request, message="Passwords do not match")
            else:
                messages.error(request, message='Username is already taken. Please use a different username')                
    return render(request, 'loginSignup/signUpScreen.html', {'form': form})







         





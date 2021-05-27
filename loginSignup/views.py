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
    return render(request, 'loginSignup/signUpScreen.html')



def createAccount(request):

    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username=form.clean_data['username'],
                    password=form.clean_data['password'],
                    email=form.clean_data['email']
                    )
            user.save()
            return HttpResponseRedirect('/')
        
    return render(request, 'loginSignup/signUpScreen.html', {'form': form})





         





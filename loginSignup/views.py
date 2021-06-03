from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import RegistrationForm
from .models import CustomUser
from challenges.models import Challenge
import json

# Create your views here.

def index(request):
    return render(request, 'loginSignup/signinScreen.html')


def signIn(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('../')
    else:
        return render(request, 'loginSignup/signinScreen.html', {'error_message': 'Incorrect Login'})




def signUp(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.cleaned_data['username']).exists():
                if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                    print(form.verify_password)
                    userCreated = User.objects.create_user(
                            username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                            email=form.cleaned_data['email'],
                            first_name=form.cleaned_data['firstName'],
                            last_name = form.cleaned_data['lastName'],
                            )

                    print(Challenge.objects.all().count())
                    print(Challenge.objects.all())
                    
                    challengesJSON = []

                    for i in range(Challenge.objects.all().count()):
                        if i != 0:
                            #TODO: CHANGE HIDDEN BACK TO TRUE
                            challenge = {f'challenge{i}': f'{i}', 'hidden': 'false', 'completed': 'false'}
                        else:
                            challenge = {f'challenge{i}': f'{i}', 'hidden': 'false', 'completed': 'false'}
                        challengesJSON.append(challenge)

                    JSONchallenges = json.dumps(challengesJSON)



                    customUser = CustomUser(numChallenges=Challenge.objects.all().count(), completedChallenges=0, challenges=JSONchallenges, user=userCreated, last_name=form.cleaned_data['lastName'])


                    userCreated.save()
                    customUser.save()




                    login(request, userCreated)
                    return HttpResponseRedirect('../../')
                else:
                    messages.error(request, message="Passwords do not match")
            else:
                messages.error(request, message='Username is already taken. Please use a different username')                
    return render(request, 'loginSignup/signUpScreen.html', {'form': form})







         





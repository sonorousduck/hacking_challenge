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
from datetime import datetime, timedelta
from customAdmin.models import AssignmentDates


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

                    email = form.cleaned_data['email']
                    if not email.endswith('usu.edu'):
                        messages.error(request, message="Use a usu.edu email")
                        return render(request, 'loginSignup/signUpScreen.html', {'form': form})

                    userCreated = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password'],
                        email=form.cleaned_data['email'],
                        first_name=form.cleaned_data['firstName'],
                        last_name=form.cleaned_data['lastName'],
                    )

                    challengesJSON = []
                    incorrectPerChallenge = []
                    JSONAchievements = json.dumps([])

                    try:
                        openTime = AssignmentDates.objects.get(
                            description="open")

                        if (openTime.date + timedelta(days=3) > datetime.now().date()):
                            achievements = json.loads(JSONAchievements)
                            achievements.append('Early Bird')
                            JSONAchievements = json.dumps(achievements)

                    except:
                        pass

                    for i in range(Challenge.objects.all().count()):
                        if i != 0:
                            challenge = {f'challenge{i + 1}': f'{i + 1}',
                                         'hidden': 'true', 'completed': 'false'}
                        else:
                            challenge = {f'challenge{i + 1}': f'{i + 1}',
                                         'hidden': 'false', 'completed': 'false'}

                        incorrectness = {
                            f'challenge{i + 1}': f'{i + 1}', 'numberIncorrect': '0'}

                        challengesJSON.append(challenge)
                        incorrectPerChallenge.append(incorrectness)

                    JSONchallenges = json.dumps(challengesJSON)
                    JSONIncorrect = json.dumps(incorrectPerChallenge)
                    numberRequiredChallenges = Challenge.objects.all().filter(
                        optionalChallenge=False).count()

                    customUser = CustomUser(numChallenges=Challenge.objects.all().count(), numRequiredChallenges=numberRequiredChallenges, completedChallenges=0, challenges=JSONchallenges, incorrectPerChallenge=JSONIncorrect, user=userCreated,
                                            first_name=form.cleaned_data['firstName'], last_name=form.cleaned_data['lastName'], achievements=JSONAchievements, customText="Look at who is too cool for flavor text or something! Psh! (Ironically, this is your flavor text")

                    userCreated.save()
                    customUser.save()

                    login(request, userCreated)
                    return HttpResponseRedirect('../../')
                else:
                    messages.error(request, message="Passwords do not match")
            else:
                messages.error(
                    request, message='Username is already taken. Please use a different username')
    return render(request, 'loginSignup/signUpScreen.html', {'form': form})

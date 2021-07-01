from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from loginSignup.models import CustomUser
import json
from achievements.models import Achievements

# Create your views here.

@login_required()
def index(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    completedChallenges = customUser.completedChallenges
    numChallenges = customUser.numChallenges
    isAdmin = customUser.admin
    firstName = request.user.first_name
    lastName = request.user.last_name
    username = request.user.username

    achievements = json.loads(customUser.achievements)
    achievementList = []

    for count, achievement in enumerate(achievements):
        achievementList.append(Achievements.objects.get(title=achievement))

    

    
    return render(request, 'homepage/index.html', {'completedChallenges': completedChallenges, 'numChallenges': numChallenges, 'isAdmin': isAdmin, 'achievements': achievementList, 'firstName': firstName, 'lastName': lastName, 'username': username})



@login_required
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('login')

@login_required
def resetFlavorText(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    customUser.customText = "Look at who is too cool for flavor text or something! Psh! (Ironically, this is your flavor text)"
    customUser.save()

    return HttpResponseRedirect(reverse("index"))

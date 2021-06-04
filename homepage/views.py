from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from loginSignup.models import CustomUser


# Create your views here.

@login_required()
def index(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    completedChallenges = customUser.completedChallenges
    numChallenges = customUser.numChallenges
    isAdmin = customUser.admin

    
    return render(request, 'homepage/index.html', {'completedChallenges': completedChallenges, 'numChallenges': numChallenges, 'isAdmin': isAdmin})




def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('login')

def resetFlavorText(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    customUser.customText = ""
    customUser.save()

    return HttpResponseRedirect(reverse("index"))

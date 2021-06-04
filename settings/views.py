from django.shortcuts import render
from loginSignup.models import CustomUser
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.


def index(request):
    

    customUser = CustomUser.objects.get(user=request.user.id)
    isAdmin = customUser.admin
    firstName = request.user.first_name
    lastName = request.user.last_name
    username = request.user.username
    customText = customUser.customText


    return render(request, 'settings/index.html', {'isAdmin': isAdmin, 'customUser': customUser, 'firstName': firstName, 'lastName': lastName, 'username': username, 'customText': customText})


def updateText(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    customUser.customText = request.POST['newText']
    customUser.save()

    return HttpResponseRedirect(reverse("settings:settings"))








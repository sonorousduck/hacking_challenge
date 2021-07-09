from django.shortcuts import render
from loginSignup.models import CustomUser
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


@login_required()
def index(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    if (request.GET):
        if ('admin' in request.GET):
            customUser.admin = request.GET['admin']
            customUser.save()

    isAdmin = customUser.admin
    firstName = request.user.first_name
    lastName = request.user.last_name
    username = request.user.username
    customText = customUser.customText


    return render(request, 'settings/index.html', {'isAdmin': isAdmin, 'customUser': customUser, 'firstName': firstName, 'lastName': lastName, 'username': username, 'customText': customText})


@login_required()
def updateText(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    

    if (request.POST):
        customUser.customText = request.POST['newText']
        customUser.save()



    return HttpResponseRedirect(reverse("settings:settings"))


@login_required()
def updatePassword(request):
    user = request.user


    if (request.POST):
        if (request.POST['password'] == request.POST['confirmPassword'] and request.POST['password'] != ''):
            user.set_password(request.POST['password'])
            user.save()

            newUser = authenticate(request, username=user.username, password=request.POST['password'])
            if newUser is not None:
                login(request, newUser)
                messages.success(request, "Password successfully changed!")
                return HttpResponseRedirect(reverse("settings:settings"))
        else:
            messages.error(request, "Passwords do not match")
            return HttpResponseRedirect(reverse("settings:settings"))



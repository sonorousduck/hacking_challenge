from django.shortcuts import render
from loginSignup.models import CustomUser
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
        if (request.POST['password'] == request.POST['confirmPassword']):
            user.set_password(request.POST['password'])
            user.save()

            return HttpResponseRedirect(reverse("settings:settings"), {"message": "success!"})
        else:
            return HttpResponseRedirect(reverse("settings:settings"), {"message": "Failed!"})







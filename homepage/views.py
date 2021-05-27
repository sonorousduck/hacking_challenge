from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

@login_required()
def index(request):
    

    return render(request, 'homepage/index.html')



def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('login')


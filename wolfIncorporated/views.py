from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LoneWolfUser
from django.http import HttpResponseRedirect


# Create your views here.


#TODO: Somehow redirect here if they don't have a Lone Wolf Account. Else go to home page of Lone Wolf

@login_required()
def index(request):
    

    if (request.GET):
        if ('EmployeeID' not in request.GET):
            print(f"Welcome {request.GET['username']}")
            print("Create user, create database stuff, and everything. Instantiate to non-admin")
           
            LoneWolfUser.objects.all().delete()

            loneWolfAgent = LoneWolfUser(admin="False", username=request.GET['username'], user=request.user,  last_name=request.user.last_name)

            loneWolfAgent.save()

            return HttpResponseRedirect('./homepage')



    return(render(request, 'wolfIncorporated/index.html'))


def homepage(request):
   




    return (render(request, 'wolfIncorporated/homepage.html'))






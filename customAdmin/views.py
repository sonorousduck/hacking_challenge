from django.shortcuts import render
from .models import AssignmentDates
from django.urls import reverse
from challenges.models import Challenge
from django.http import HttpResponseRedirect, HttpResponseForbidden
from datetime import datetime
from django.contrib.auth.decorators import login_required
from matplotlib import pyplot as plt

# Create your views here.

@login_required
def index(request):
    dates = AssignmentDates.objects.all()
    


    if (request.user.is_superuser):
        allChallenges = Challenge.objects.all().order_by('-totalIncorrectGuesses')
        allChallengesNoOrder = Challenge.objects.all()

        incorrectGuesses = []
        orderChallenges = []

        for challenge in allChallengesNoOrder:
            incorrectGuesses.append(challenge.totalIncorrectGuesses)
            orderChallenges.append(str(challenge.order))

        plt.xlabel('Challenges')
        plt.ylabel('Incorrect Guesses Total')
        plt.bar(orderChallenges, incorrectGuesses, align='center', alpha=0.6)
        plt.savefig('static/customAdmin/incorrectGuesses.png')

        return render(request, 'customAdmin/index.html', {'dates': dates, 'allChallenges': allChallenges})
    else: 
        return HttpResponseForbidden("403 Forbidden")



@login_required
def changeDate(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden("403 Forbidden")


    startDate = request.POST['startDate']
    startTime = request.POST['startTime']

    endDate = request.POST['endDate']
    endTime = request.POST['endTime']

    if startDate != '' or startTime != '':
        try:
            openDate = AssignmentDates.objects.get(description="open")
            
            if startDate != '':
                openDate.date = startDate
            if startTime != '':
                openDate.time = startTime

            openDate.save()
        except:
            if startDate == '':
                openDate = AssignmentDates(time=startTime, description="open")

            elif startTime == '':
                openDate = AssignmentDates(date=startDate, description="open")

            else:
                openDate = AssignmentDates(date=startDate, time=startTime, description="open")
            
            openDate.save()

    if endDate != '' or endTime != '':
        try:
            closedDate = AssignmentDates.objects.get(description="closed")
            
            if endDate != '':
                closedDate.date = endDate
            if endTime != '':
                closedDate.time = endTime
            
            closedDate.save()
        except:
            if endDate == '':
                closedDate = AssignmentDates(time=endTime, description="closed")
            
            elif endTime == '':
                closedDate = AssignmentDates(date=endDate, description="closed")

            else:
                closedDate = AssignmentDates(date=endDate, time=endTime, description="closed")
            
            closedDate.save()


    return HttpResponseRedirect(reverse('customAdmin:index'))


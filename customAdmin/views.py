from django.shortcuts import render
from .models import AssignmentDates
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    dates = AssignmentDates.objects.all()
    


    if (request.user.is_superuser):
        return render(request, 'customAdmin/index.html', {'dates': dates})
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

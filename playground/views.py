from django.shortcuts import render
from .models import Testing
from django.utils import timezone
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse


# Create your views here.


def index(request): 
    return render(request, 'playground/index.html')


def getDatabaseData(request):

    allData = Testing.objects.all()
    JSONobj = []


    # Create the JSON object

    for obj in allData:
        JSONobj.append({'description': obj.description, 'date': obj.date, 'completed': obj.completed})


    response = JsonResponse(JSONobj, safe=False)
    response['Access-Control-Allow-Origin'] = '*'

    return response



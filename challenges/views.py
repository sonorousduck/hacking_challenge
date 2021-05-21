from django.shortcuts import render
from .models import Challenge, Hint
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'challenges/index.html')



def getChallenges(request):
    allData = Challenge.objects.all()
    JSONobj = []


    # Create the JSON object

# TODO: Change this to not include any sensitive data, i.e. the flag. That will have to be done in a validation request when an answer is submitted.


    for obj in allData:
        JSONobj.append({'title': obj.title, 'description': obj.description, 'order' : obj.order, 'hidden' : obj.hidden, 'pointValue' : obj.hidden, 'optionalChallenge': obj.optionalChallenge, 'difficultyIndicator': obj.difficultyIndicator})


    response = JsonResponse(JSONobj, safe=False)
    response['Access-Control-Allow-Origin'] = '*'

    return response



from django.shortcuts import render, get_object_or_404
from .models import Challenge, Hint
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    challenges = Challenge.objects.order_by('order')
    return render(request, 'challenges/index.html', {'challenges': challenges})


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

#def navigateToChallenge(request):
#    print(request)
#    return render(request, f'challenges/challenge1.html')

def challengeDetails(request, challenge_id):
    challenge = get_object_or_404(Challenge, order=challenge_id - 1)
    return render(request, f'challenges/challenge{challenge_id - 1}.html', {'challenge': challenge})


from django.shortcuts import render, get_object_or_404
from .models import Challenge, Hint
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    challenges = Challenge.objects.order_by('order')
    return render(request, 'challenges/index.html', {'challenges': challenges})


def validation(request):
    if (request.method == "POST"):
        json_response = [] 

        challenge = Challenge.objects.get(order=request.POST['challenge_id'])

        print(challenge)

        # Create the JSON object

        if (challenge.flag == request.POST['passcode']):
            json_response.append({'success': True})
        else:
            json_response.append({'success': False})

        response = JsonResponse(json_response, safe=False)
        response['Access-Control-Allow-Origin'] = '*'

        return response

# TODO: Get the information for which challenge to send them to from a database instead of static as I am currently doing. This allows us to easier change the order of the levels and it will correctly point to the html page that it should. Essentially, it will be a dictionary mapping the challenge to a html page (instead of currently the order mapping it strictly to an html page, which makes it if the order changes, then it doesn't update correctly to the new html page

def challengeDetails(request, challenge_id):
    challenge = get_object_or_404(Challenge, order=challenge_id - 1)
    return render(request, f'challenges/challenge{challenge_id - 1}.html', {'challenge': challenge})


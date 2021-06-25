from django.shortcuts import render, get_object_or_404
from .models import Challenge, Hint
from loginSignup.models import CustomUser
from achievements.models import Achievements
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseForbidden 
from django.contrib.auth.decorators import login_required
import json


@login_required()
def index(request):
    easyChallenges = Challenge.objects.filter(difficultyIndicator="Easy").order_by('order')
    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)
    count = 0

    for challenge in easyChallenges:
        challenge.hidden = data[count]['hidden']
        challenge.completed = data[count]['completed']
        challenge.data = data[count]
        count += 1

    intermediateChallenges = Challenge.objects.filter(difficultyIndicator="Intermediate").order_by('order')

    for challenge in intermediateChallenges:
        challenge.hidden = data[count]['hidden']
        challenge.completed = data[count]['completed']
        challenge.data = data[count]
        count += 1


    return render(request, 'challenges/index.html', {'easyChallenges': easyChallenges, 'intermediateChallenges': intermediateChallenges})


@login_required()
def validation(request):
    if (request.method == "POST"):
        json_response = [] 

        challenge = Challenge.objects.get(order=request.POST['challenge_id'])
        customUser = CustomUser.objects.get(user=request.user.id)
        challenge_id = int(request.POST['challenge_id'])

        # Create the JSON object

        if (challenge.flag == request.POST['passcode']):
            json_response.append({'success': True})
            data = json.loads(customUser.challenges)
            incorrectPerChallengeData = json.loads(customUser.incorrectPerChallenge)
            
            if data[challenge_id]['completed'] != 'true':
                customUser.completedChallenges += 1
                data[challenge_id]['completed'] = 'true'
                data[challenge_id + 1]['hidden'] = 'false'

                flawlessInARow = 0


                for i in range(challenge_id, -1, -1):
                    if incorrectPerChallengeData[i]['numberIncorrect'] == "0":
                        flawlessInARow += 1
                    else:
                        break

                
                if (flawlessInARow % 8) == 2:
                    achievements = json.loads(customUser.achievements)
                    achievements.append('2 down')
                    customUser.achievements = json.dumps(achievements)

                if (flawlessInARow % 8) == 3:
                    achievements = json.loads(customUser.achievements)
                    achievements.append('3 down')
                    customUser.achievements = json.dumps(achievements)

                if (flawlessInARow % 8) == 4:
                    achievements = json.loads(customUser.achievements)
                    achievements.append('Breathtaking')
                    customUser.achievements = json.dumps(achievements)

                if (flawlessInARow % 8) == 5:
                    achievements = json.loads(customUser.achievements)
                    achievements.append('Phenomenal')
                    customUser.achievements = json.dumps(achievements)

                if (flawlessInARow % 8) == 6:
                    achievements = json.loads(customUser.achievements)
                    achievements.append('Unstoppable')
                    customUser.achievements = json.dumps(achievements)

                if (flawlessInARow % 8) == 7:
                    achievements = json.loads(customUser.achievements)
                    achievements.append('Unforgettable')
                    customUser.achievements = json.dumps(achievements)

                if (flawlessInARow % 8) == 0 and flawlessInARow > 0:
                    achievements = json.loads(customUser.achievements)
                    achievements.append('Ascended')
                    customUser.achievements = json.dumps(achievements)
                
                if flawlessInARow == len(customUser.challenges):
                    achievements = json.loads(customUser.achievements)
                    achievements.append('Flawless')
                    customUser.achievements = json.dumps(achievements)


                customUser.challenges = json.dumps(data)
                customUser.save()



        else:
            json_response.append({'success': False})

            data = json.loads(customUser.challenges)
            incorrectPerChallengeData = json.loads(customUser.incorrectPerChallenge)

            if data[challenge_id]['completed'] != 'true':
                numIncorrect = int(incorrectPerChallengeData[challenge_id]['numberIncorrect'])
                numIncorrect += 1
                customUser.numTotalIncorrectGuesses += 1
                incorrectPerChallengeData[challenge_id]['numberIncorrect'] = str(numIncorrect)
                customUser.incorrectPerChallenge = json.dumps(incorrectPerChallengeData)
                customUser.save()


        response = JsonResponse(json_response, safe=False)
        response['Access-Control-Allow-Origin'] = '*'

        return response

# TODO: Get the information for which challenge to send them to from a database instead of static as I am currently doing. This allows us to easier change the order of the levels and it will correctly point to the html page that it should. Essentially, it will be a dictionary mapping the challenge to a html page (instead of currently the order mapping it strictly to an html page, which makes it if the order changes, then it doesn't update correctly to the new html page

@login_required()
def challengeDetails(request, challenge_id):
    loneWolfID = [14, 15, 16, 17]
    if challenge_id in loneWolfID:
        challenge = get_object_or_404(Challenge, order=challenge_id + 86)
    else:
        challenge = get_object_or_404(Challenge, order=challenge_id - 1)

    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)

    challenge.data = data[int(challenge_id) - 1]
    if (challenge_id < Challenge.objects.all().count()):
        challenge.nextChallenge = data[int(challenge_id)]['hidden']
        challenge.nextChallengeID = int(challenge_id) + 1

    if challenge.data['hidden'] == 'true':
        return HttpResponse(render(request, 'challenges/forbidden.html'))
    
    if challenge.challengeSeries == "LoneWolf":
        return render(request, f'challenges/loneWolfPart{challenge.title[-1]}.html', {'challenge': challenge})



    return render(request, f'challenges/challenge{challenge_id - 1}.html', {'challenge': challenge})

@login_required()
def passwordSecurity(request):
    return HttpResponse(200);

@login_required()
def security(request):
    challenge = Challenge.objects.get(order=6)


    if not request.GET:
        return HttpResponse("not authorized")
    elif request.GET['username'] and request.GET['password']:
        return HttpResponse(challenge.flag)
    else:
        return HttpResponse("username must not be NULL and password must not be NULL")

@login_required()
def securityValidation(request):
    challenge = Challenge.objects.get(order=7)
    

    if not request.GET:
        return HttpResponse("Not Authorized")

    elif request.GET['password'] == "":
        return HttpResponse("bash: "": command not found")
    elif request.GET['password'] == "ls":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt")
    elif request.GET['password'] == "ls -a":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt .env")
    elif request.GET['password'] == "cat .env":
        return HttpResponse(challenge.flag)
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat someotherfile.txt":
        return HttpResponse("Contents of someotherfile.txt")
    elif request.GET['password'] == "cat cleverlynamedfile.txt":
        return HttpResponse("Contents of cleverlynamedfile.txt")
    elif request.GET['password'] == "pwd":
        return HttpResponse("../security/dbvalidation")
    elif request.GET['password'] == "cd":
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    elif request.GET['password'].startswith("cat"):
        return HttpResponse("This file doesn't exist")
    elif request.GET['password'].startswith("cp") or request.GET['password'].startswith("mv") or request.GET['password'].startswith("touch") or  request.GET['password'].startswith("rm") or request.GET['password'].startswith("locate") or  request.GET['password'].startswith("grep"):
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    else:
        return HttpResponse(f"bash: {request.GET['password']}: command not found")


# TODO: Add the cookie into the database, then I can just serve this actual file when they cat views.py instead
# TODO: Beef up the ls. Have it list all of the files instead of just views.py (Have it ls urls.py, etc. etc.

@login_required()
def secure(request):
    # Just in case I forget the password... Its 1a2s3d4f5g6h7j8k9l
    if not request.GET:
        return HttpResponse("Not Authorized")
    elif request.GET['password'] == "":
        return HttpResponse("Invalid Command") 
    elif request.GET['password'] == "ls":
        return HttpResponse("views.py\n")
    elif request.GET['password'] == "ls -a":
        return HttpResponse("views.py\n")
    elif request.GET['password'] == "cat views.py":
        return HttpResponse(leak, content_type='text/plain')
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat someotherfile.txt":
        return HttpResponse("Contents of someotherfile.txt")
    elif request.GET['password'] == "cat cleverlynamedfile.txt":
        return HttpResponse("Contents of cleverlynamedfile.txt")
    elif request.GET['password'] == "pwd":
        return HttpResponse("../security/validation")
    elif request.GET['password'] == "cd":
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    elif request.GET['password'].startswith("cat"):
        return HttpResponse("This file doesn't exist")
    elif request.GET['password'].startswith("cp") or request.GET['password'].startswith("mv") or request.GET['password'].startswith("touch") or  request.GET['password'].startswith("rm") or  request.GET['password'].startswith("locate") or request.GET['password'].startswith("locate") or  request.GET['password'].startswith("grep"):
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    else:
        return HttpResponse(f"bash: {request.GET['password']}: command not found")

@login_required()
def cookieValidation(request):
    challenge = Challenge.objects.get(order=9)
    if request.POST['password'] == '':
        return HttpResponse("Not Authorized")
    elif request.COOKIES.get('ryansbestta') == 'spamspamspamspamspamspameggsspam':
        return HttpResponse(challenge.flag)
    else: 
        return HttpResponse("Not Authorized")


@login_required()
def adminLogin(request):
    # TODO: Fix this one a bit. Right now, it works to do the javascript brute force. however there is a caveat. When you find the 200 response code, if you try double clicking it, you get hit with the CSRF_token missing right now. You can, however, look into the request and pull the password and username from it. Which might actually be a feature instead of a bug, since Django actually protects against this kind of thing specifically, so it takes one extra step to figure it out.

    # TODO: Set this one up too to use a database instead of the hardcoded values

    if request.POST['username'] == 'ShadyVelociraptor@gmail.com' and request.POST['password'] == 'turtle':
    
        
        challenge = Challenge.objects.get(order=10)
        
        return HttpResponse(challenge.flag)

    else:
        return HttpResponseForbidden("""

            <h1 style="align:center; text-align: center"> 403 Forbidden </h1>
            <h5 style="align:center; text-align: center"> Leave this page or suffer the consequences </h5>

        """)
    


leak = """
from django.shortcuts import render, get_object_or_404
from .models import Challenge, Hint
from loginSignup.models import CustomUser
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseForbidden 
from django.contrib.auth.decorators import login_required
import json


@login_required()
def index(request):
    challenges = Challenge.objects.order_by('order')
    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)

    for count, challenge in enumerate(challenges):
        challenge.hidden = data[count]['hidden']
        challenge.completed = data[count]['completed']
        challenge.data = data[count]


    return render(request, 'challenges/index.html', {'challenges': challenges})


@login_required()
def validation(request):
    if (request.method == "POST"):
        json_response = [] 

        challenge = Challenge.objects.get(order=request.POST['challenge_id'])
        customUser = CustomUser.objects.get(user=request.user.id)
        print(challenge)
        challenge_id = int(request.POST['challenge_id'])

        # Create the JSON object

        if (challenge.flag == request.POST['passcode']):
            json_response.append({'success': True})
            data = json.loads(customUser.challenges)

            if data[challenge_id]['completed'] != 'true':
                customUser.completedChallenges += 1
                data[challenge_id]['completed'] = 'true'
                data[challenge_id + 1]['hidden'] = 'false'
                customUser.challenges = json.dumps(data)
                customUser.save()



        else:
            json_response.append({'success': False})

        response = JsonResponse(json_response, safe=False)
        response['Access-Control-Allow-Origin'] = '*'

        return response

# TODO: Get the information for which challenge to send them to from a database instead of static as I am currently doing. This allows us to easier change the order of the levels and it will correctly point to the html page that it should. Essentially, it will be a dictionary mapping the challenge to a html page (instead of currently the order mapping it strictly to an html page, which makes it if the order changes, then it doesn't update correctly to the new html page

@login_required()
def challengeDetails(request, challenge_id):
    challenge = get_object_or_404(Challenge, order=challenge_id - 1)

    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)

    challenge.data = data[int(challenge_id) - 1]
    if (challenge_id < Challenge.objects.all().count()):
        challenge.nextChallenge = data[int(challenge_id)]['hidden']
        challenge.nextChallengeID = int(challenge_id) + 1

    if challenge.data['hidden'] == 'true':
        return HttpResponse(render(request, 'challenges/forbidden.html'))

    return render(request, f'challenges/challenge{challenge_id - 1}.html', {'challenge': challenge})

@login_required()
def passwordSecurity(request):
    return HttpResponse(200);

@login_required()
def security(request):
    challenge = Challenge.objects.get(order=6)


    if not request.GET:
        return HttpResponse("not authorized")
    elif request.GET['username'] and request.GET['password']:
        return HttpResponse(challenge.flag)
    else:
        return HttpResponse("username must not be NULL and password must not be NULL")

@login_required()
def securityValidation(request):
    challenge = Challenge.objects.get(order=7)
    

    if not request.GET:
        return HttpResponse("Not Authorized")

    elif request.GET['password'] == "":
        return HttpResponse("bash: "": command not found")
    elif request.GET['password'] == "ls":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt")
    elif request.GET['password'] == "ls -a":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt .env")
    elif request.GET['password'] == "cat .env":
        return HttpResponse(challenge.flag)
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat someotherfile.txt":
        return HttpResponse("Contents of someotherfile.txt")
    elif request.GET['password'] == "cat cleverlynamedfile.txt":
        return HttpResponse("Contents of cleverlynamedfile.txt")
    elif request.GET['password'] == "pwd":
        return HttpResponse("../security/dbvalidation")
    elif request.GET['password'] == "cd":
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    elif request.GET['password'].startswith("cat"):
        return HttpResponse("This file doesn't exist")
    elif request.GET['password'].startswith("cp") or request.GET['password'].startswith("mv") or request.GET['password'].startswith("touch") or  request.GET['password'].startswith("rm") or  request.GET['password'].startswith("locate") or request.GET['password'].startswith("locate") or  request.GET['password'].startswith("grep"):
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    else:
        return HttpResponse(f"bash: {request.GET['password']}: command not found")


# TODO: Add the cookie into the database, then I can just serve this actual file when they cat views.py instead
# TODO: Beef up the ls. Have it list all of the files instead of just views.py (Have it ls urls.py, etc. etc.

@login_required()
def secure(request):
    # Just in case I forget the password... Its 1a2s3d4f5g6h7j8k9l
    if not request.GET:
        return HttpResponse("Not Authorized")
    elif request.GET['password'] == "":
        return HttpResponse("Invalid Command") 
    elif request.GET['password'] == "ls":
        return HttpResponse("views.py\n")
    elif request.GET['password'] == "ls -a":
        return HttpResponse("views.py\n")
    elif request.GET['password'] == "cat views.py":
        return HttpResponse(leak, content_type='text/plain')
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat somefile.txt":
        return HttpResponse("Contents of somefile.txt")
    elif request.GET['password'] == "cat someotherfile.txt":
        return HttpResponse("Contents of someotherfile.txt")
    elif request.GET['password'] == "cat cleverlynamedfile.txt":
        return HttpResponse("Contents of cleverlynamedfile.txt")
    elif request.GET['password'] == "pwd":
        return HttpResponse("../security/validation")
    elif request.GET['password'] == "cd":
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    elif request.GET['password'].startswith("cat"):
        return HttpResponse("This file doesn't exist")
    elif request.GET['password'].startswith("cp") or request.GET['password'].startswith("mv") or request.GET['password'].startswith("touch") or  request.GET['password'].startswith("rm") or  request.GET['password'].startswith("locate") or request.GET['password'].startswith("locate") or  request.GET['password'].startswith("grep"):
        return HttpResponse("This command has been scrubbed and we know what you are trying to do!")
    else:
        return HttpResponse(f"bash: {request.GET['password']}: command not found")

@login_required()
def cookieValidation(request):
    challenge = Challenge.objects.get(order=9)
    if request.POST['password'] == '':
        return HttpResponse("Not Authorized")
    elif request.COOKIES.get('ryansbestta') == 'spamspamspamspamspamspameggsspam':
        return HttpResponse(challenge.flag)
    else: 
        return HttpResponse("Not Authorized")
"""

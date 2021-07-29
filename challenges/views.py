from django.shortcuts import render, get_object_or_404
from .models import Challenge, Hint
from loginSignup.models import CustomUser
from customAdmin.models import AssignmentDates
from achievements.models import Achievements
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseForbidden 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime, timedelta


@login_required()
def index(request):
    easyChallenges = Challenge.objects.filter(difficultyIndicator="Easy").order_by('order')
    moderateChallenges = Challenge.objects.filter(difficultyIndicator="Moderate").order_by('order')
    hardChallenges = Challenge.objects.filter(difficultyIndicator="Hard").order_by('order')
    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)
    count = 0
    easyCompleted = 0
    currentEasyChallenge = easyChallenges[0].order + 1
    foundCurrentChallenge = False

    for challenge in easyChallenges:
        challenge.hidden = data[count]['hidden']
        challenge.completed = data[count]['completed']
        challenge.data = data[count]
        if data[count]['completed'] == 'true':
            easyCompleted += 1
            if easyCompleted != len(easyChallenges):
                if data[count + 1]['completed'] == 'false':
                    currentEasyChallenge = easyChallenges[count + 1].order + 1
            else: 
                currentEasyChallenge = 'completed'

        count += 1
        
        if easyCompleted < len(easyChallenges) - 3:
            moderateLocked = 'true'
        else:
            moderateLocked = 'false'

        if easyCompleted == len(easyChallenges):

            hardLocked = 'false'
            hardChallengesCount = len(hardChallenges)
            for i in range(hardChallengesCount):
                data[len(moderateChallenges) + len(easyChallenges) + i]['hidden'] = 'false'
            customUser.challenges = json.dumps(data)
            customUser.save()

        else:
            hardLocked = 'true'

    if moderateLocked == 'false':
        data[len(easyChallenges)]['hidden'] = 'false'
        customUser.challenges = json.dumps(data)
        customUser.save()

    moderateCompleted = 0
    moderateFound = False
    
    for challenge in moderateChallenges:
        challenge.hidden = data[count]['hidden']
        challenge.completed = data[count]['completed']
        challenge.data = data[count]
        if data[count]['completed'] == 'true':
            moderateCompleted += 1
            if moderateCompleted != len(moderateChallenges):
                if data[count + 1]['completed'] == 'false':
                    currentModerateChallenge = moderateChallenges[count - len(easyChallenges) + 1].order + 1 
                    moderateFound = True
            else:
                currentModerateChallenge = 'completed'
        else:
            if not moderateFound:
                currentModerateChallenge = moderateChallenges[0].order + 1
        count += 1

    if moderateCompleted == len(moderateChallenges):
        hardLocked = 'false'
        hardChallengesCount = len(hardChallenges)
        for i in range(hardChallengesCount):
            data[len(moderateChallenges) + len(easyChallenges) + i]['hidden'] = 'false'
        customUser.challenges = json.dumps(data)
        customUser.save()

    hardCompleted = 0
    hardFound = False

    for challenge in hardChallenges:
        challenge.hidden = data[count]['hidden']
        challenge.completed = data[count]['completed']
        challenge.data = data[count]
        if data[count]['completed'] == 'true':
            hardCompleted += 1
            if hardCompleted != len(hardChallenges):
                if data[count + 1]['completed'] == 'false':
                    currentHardChallenge = hardChallenges[count - len(easyChallenges) - len(moderateChallenges) + 1].order + 1
                    hardFound = True
            else:
                currentHardChallenge = 'completed'
        else:
            if not hardFound:
                currentHardChallenge = hardChallenges[0].order + 1
        count += 1

    return render(request, 'challenges/index.html', {'easyChallenges': easyChallenges, 'moderateChallenges': moderateChallenges, 'hardChallenges': hardChallenges, 'easyCompleted': easyCompleted, 'moderateCompleted': moderateCompleted, 'hardCompleted': hardCompleted, 'moderateLocked': moderateLocked, 'hardLocked': hardLocked, 'currentEasyChallenge': currentEasyChallenge, 'currentModerateChallenge': currentModerateChallenge, 'currentHardChallenge': currentHardChallenge})


@login_required()
def validation(request):
    if (request.method == "POST"):
        

        json_response = [] 
        allGood = True

        if (AssignmentDates.objects.all()):
            currentTime = datetime.now().time()
            currentDate = datetime.today().date()

            openDate = AssignmentDates.objects.get(description="open")
            closeDate = AssignmentDates.objects.get(description="closed")
            

            if currentDate < openDate.date or currentDate > closeDate.date:
                allGood = False

            if currentDate > openDate.date and currentDate < closeDate.date:
                if (currentTime > closeDate.time and currentTime == closeDate.date) or (currentTime < openDate.time and currentTime == openDate.date):
                    allGood = False
        if allGood:

            loneWolfID = [100, 101, 102, 103]
            challenge_id = int(request.POST['challenge_id'])
            challenge = Challenge.objects.get(order=challenge_id)
            
            if challenge_id in loneWolfID:
                challenge_id_CustomUser = challenge_id - 87
            else:
                challenge_id_CustomUser = challenge_id

            customUser = CustomUser.objects.get(user=request.user.id)
            challenge_id = int(request.POST['challenge_id'])

            # Create the JSON object

            if (challenge.flag == request.POST['passcode'].strip()):
                json_response.append({'success': True})
                data = json.loads(customUser.challenges)
                incorrectPerChallengeData = json.loads(customUser.incorrectPerChallenge)

                if data[challenge_id_CustomUser]['completed'] != 'true':
                    customUser.completedChallenges += 1
                    customUser.correctInARow += 1
                    customUser.percentComplete =  (customUser.completedChallenges / customUser.numRequiredChallenges) * 100
                    if customUser.percentComplete > 100:
                        customUser.percentComplete = 100
                    
                    data[challenge_id_CustomUser]['completed'] = 'true'
    #TODO: Add a better catch for you are done
                    if not challenge_id_CustomUser + 1 > len(Challenge.objects.all()) - 1:

                        data[challenge_id_CustomUser + 1]['hidden'] = 'false'



                    if (customUser.correctInARow % 8) == 2:
                        achievements = json.loads(customUser.achievements)
                        achievements.append('2 down')
                        customUser.achievements = json.dumps(achievements)

                    if (customUser.correctInARow % 8) == 3:
                        achievements = json.loads(customUser.achievements)
                        achievements.append('3 down')
                        customUser.achievements = json.dumps(achievements)

                    if (customUser.correctInARow % 8) == 4:
                        achievements = json.loads(customUser.achievements)
                        achievements.append('Breathtaking')
                        customUser.achievements = json.dumps(achievements)

                    if (customUser.correctInARow % 8) == 5:
                        achievements = json.loads(customUser.achievements)
                        achievements.append('Phenomenal')
                        customUser.achievements = json.dumps(achievements)

                    if (customUser.correctInARow % 8) == 6:
                        achievements = json.loads(customUser.achievements)
                        achievements.append('Unstoppable')
                        customUser.achievements = json.dumps(achievements)

                    if (customUser.correctInARow % 8) == 7:
                        achievements = json.loads(customUser.achievements)
                        achievements.append('Unforgettable')
                        customUser.achievements = json.dumps(achievements)

                    if (customUser.correctInARow % 8) == 0 and customUser.correctInARow > 0:
                        achievements = json.loads(customUser.achievements)
                        achievements.append('Ascended')
                        customUser.achievements = json.dumps(achievements)
                    
                    if  customUser.correctInARow == len(customUser.challenges):
                        achievements = json.loads(customUser.achievements)
                        achievements.append('Flawless')
                        customUser.achievements = json.dumps(achievements)


                    customUser.challenges = json.dumps(data)
                    customUser.save()



            else:
                json_response.append({'success': False})

                data = json.loads(customUser.challenges)
                incorrectPerChallengeData = json.loads(customUser.incorrectPerChallenge)

                if data[challenge_id_CustomUser]['completed'] != 'true':
                    numIncorrect = int(incorrectPerChallengeData[challenge_id_CustomUser]['numberIncorrect'])
                    numIncorrect += 1
                    customUser.numTotalIncorrectGuesses += 1
                    customUser.correctInARow = 0
                    incorrectPerChallengeData[challenge_id_CustomUser]['numberIncorrect'] = str(numIncorrect)
                    customUser.incorrectPerChallenge = json.dumps(incorrectPerChallengeData)
                    customUser.save()


            response = JsonResponse(json_response, safe=False)
            response['Access-Control-Allow-Origin'] = '*'

            return response
        else:
            json_response.append({'success': "Assignment is closed"})
            response = JsonResponse(json_response, safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            return response



@login_required()
def challengeDetails(request, order):
    challengeID = order
    order = order - 1

    challenge = get_object_or_404(Challenge, order=order)
    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)
    admin = customUser.admin
    adminFlag = ''

    if admin:
        adminFlag = Challenge.objects.get(templateValue=12).flag


    challenge.data = data[order]
    if (challengeID < Challenge.objects.all().count()):
        challenge.nextChallenge = data[challengeID]['hidden']
        challenge.nextChallengeID = challengeID + 1
        challenge.nextUnlocked = data[challengeID - 1]['completed']
    else:
        challenge.nextUnlocked = 'last'

    if challenge.data['hidden'] == 'true':
        return HttpResponse(render(request, 'challenges/forbidden.html'))

    return render(request, f'challenges/{challenge.templateValue}.html', {'challenge': challenge, 'admin': admin, 'adminFlag': adminFlag})

@login_required()
def hardChallenges(request):
    hardChallenges = Challenge.objects.filter(difficultyIndicator="Hard")
    customUser = CustomUser.objects.get(user=request.user)
    deleted = customUser.completedAllChallenges

    bruteForce = hardChallenges[0].order + 1
    bruteForceComplete = 'false'
    crossSite = hardChallenges[1].order + 1
    crossSiteComplete = 'false'
    cryptology = hardChallenges[2].order + 1
    cryptologyComplete = 'false'
    completed = False

    challengesData = json.loads(customUser.challenges)
    if challengesData[cryptology - 1]['completed'] == 'true':
        cryptologyComplete = 'true'

    if challengesData[bruteForce - 1]['completed'] == 'true':
        bruteForceComplete = 'true'

    if challengesData[crossSite - 1]['completed'] == 'true':
        crossSiteComplete = 'true'

    if cryptologyComplete == 'true' and bruteForceComplete == 'true' and crossSiteComplete == 'true':
        completed = True

    return render(request, 'challenges/hardChallenges.html', {'cryptology': cryptology, 'bruteForce': bruteForce, 'crossSite': crossSite, 'cryptologyComplete': cryptologyComplete, 'bruteForceComplete': bruteForceComplete, 'crossSiteComplete': crossSiteComplete, 'completed': completed, 'deleted': deleted})



@login_required()
def completed(request):
    challenges = Challenge.objects.all()
    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)
    completedChallenges = []

    for count, challenge in enumerate(challenges):
        if data[count]['completed'] == 'true':
            completedChallenges.append(challenge)
    return render(request, 'challenges/allChallenges.html', {'completedChallenges': completedChallenges})
    #return HttpResponse("Congrats! You have finished this level of difficulty!", request)

@login_required()
def allChallenges(request):

    challenges = Challenge.objects.all()
    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.challenges)
    completedChallenges = []


    for count, challenge in enumerate(challenges):
        challenge.completed = data[count]['completed']
        if data[count]['completed'] == 'true':
            completedChallenges.append(challenge)



    return render(request, 'challenges/allChallenges.html', {'completedChallenges': completedChallenges})


@login_required
def deleteServer(request):
    customUser = CustomUser.objects.get(user=request.user.id)
    data = json.loads(customUser.achievements)

    if (request.headers['Config']): 
        if not customUser.completedAllChallenges:
            customUser.completedAllChallenges = True
            data.append('Rick Rolled')
            customUser.achievements = json.dumps(data)
            customUser.save()

        return HttpResponseRedirect(reverse('homepage:index'));
    else:
        return HttpResponseRedirect(reverse('homepage:index'));



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
    challenge = Challenge.objects.get(templateValue=7)
    

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
def anotherRequest(request):

    try:

        if (request.headers['allowed']):
            flag = Challenge.objects.get(templateValue=3).flag
            data = [{'flag': flag}]

            return JsonResponse(data, safe=False)
    except KeyError:
        return JsonResponse({"Yeah No": "Good try though :)"}, safe=False)


@login_required()
def cookieValidation(request):
    challenge = Challenge.objects.get(order=9)
    if request.COOKIES.get('FORSPARTA!') == 'HYAAAAAA!HYAAAAAA!HYAAAAAA!':
        return HttpResponse(challenge.flag)
    else: 
        return HttpResponse("Not Authorized")


@login_required()
def hardAdminLogin(request):
    if request.POST['username'] == 'Monkey@monkey.com' and request.POST['password'] == 'yamaha':
        challenge = Challenge.objects.get(templateValue=11)
        
        return HttpResponse(challenge.flag)

    else:
        return HttpResponseForbidden("""

            <h1 style="align:center; text-align: center"> 403 Forbidden </h1>
            <h5 style="align:center; text-align: center"> Leave this page or suffer the consequences </h5>

        """)
    





@login_required()
def adminLogin(request):
    if request.POST['username'] == 'ShadyVelociraptor@gmail.com' and request.POST['password'] == 'turtle':
    
        
        challenge = Challenge.objects.get(templateValue=10)
        
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

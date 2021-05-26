from django.shortcuts import render, get_object_or_404
from .models import Challenge, Hint
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseForbidden 

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

def passwordSecurity(request):
    return HttpResponse(200);

def security(request):
    if not request.GET:
        return HttpResponse("not authorized")
    elif request.GET['username'] and request.GET['password']:
        return HttpResponse("@U/*D4(DV}wT{F`e")
    else:
        return HttpResponse("username must not be NULL and password must not be NULL")

def securityValidation(request):
    if not request.GET:
        return HttpResponse("Not Authorized")

    elif request.GET['password'] == "":
        return HttpResponse("bash: "": command not found")
    elif request.GET['password'] == "ls":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt")
    elif request.GET['password'] == "ls -a":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt .env")
    elif request.GET['password'] == "cat .env":
        return HttpResponse("/D3<]3v34Q3H,tDn")
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

def cookieValidation(request):
    print(request.POST)

    if request.POST['password'] == '':
        return HttpResponse("Not Authorized")
    elif request.COOKIES.get('ryansbestta') == 'spamspamspamspamspamspameggsspam':
        return HttpResponse(cookie_password)
    else: 
        return HttpResponse("Not Authorized")


def adminLogin(request):
    # TODO: Fix this one a bit. Right now, it works to do the javascript brute force. however there is a caveat. When you find the 200 response code, if you try double clicking it, you get hit with the CSRF_token missing right now. You can, however, look into the request and pull the password and username from it. Which might actually be a feature instead of a bug, since Django actually protects against this kind of thing specifically, so it takes one extra step to figure it out.

    # TODO: Set this one up too to use a database instead of the hardcoded values

    if request.POST['username'] == 'ShadyVelociraptor@gmail.com' and request.POST['password'] == 'turtle':
        return HttpResponse("RARW101010RKDFJLS")
    else:
        return HttpResponseForbidden("""

            <h1 style="align:center; text-align: center"> 403 Forbidden </h1>
            <h5 style="align:center; text-align: center"> Leave this page or suffer the consequences </h5>

        """)
    




cookie_password = "er4w{^a=Z,dGeyF="

leak = """
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

def passwordSecurity(request):
    return HttpResponse(200);

def security(request):
    if not request.GET:
        return HttpResponse("not authorized")
    elif request.GET['username'] and request.GET['password']:
        return HttpResponse("@U/*D4(DV}wT{F`e")
    else:
        return HttpResponse("username must not be NULL and password must not be NULL")

def securityValidation(request):
    if not request.GET:
        return HttpResponse("Not Authorized")

    elif request.GET['password'] == "":
        return HttpResponse("bash: "": command not found")
    elif request.GET['password'] == "ls":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt")
    elif request.GET['password'] == "ls -a":
        return HttpResponse("somefile.txt\nsomeotherfile.txt\ncleverlynamedfile.txt .env")
    elif request.GET['password'] == "cat .env":
        return HttpResponse("/D3<]3v34Q3H,tDn")
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

def secure(request):
    # Just in case I forget the password... Its 1a2s3d4f5g6h7j8k9l
    if not request.GET:
        return HttpResponse("Not Authorized")
    elif request.GET['password'] == "":
        return HttpResponse("Invalid Command") 
    elif request.GET['password'] == "ls":
        return HttpResponse("__init__.py\n")
    elif request.GET['password'] == "ls -a":
        return HttpResponse("__init__.py\n")
    elif request.GET['password'] == "cat __init__.py":
        return HttpResponse(leak)
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



    def cookieValidation(request):

        if request.POST['password'] == '':
            return HttpResponse("Not Authorized")
        elif request.COOKIES.get('ryansbestta') == 'spamspamspamspamspamspameggsspam':
            return HttpResponse(cookie_password)
        else: 
            return HttpResponse("Not Authorized")
"""

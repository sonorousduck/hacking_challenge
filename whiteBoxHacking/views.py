from django.shortcuts import render
from django.http import HttpResponse
from challenges.models import Challenge
import os
import subprocess
import re
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    return render(request, 'whiteBoxHacking/index.html')

@login_required()
def showViews(request):
    return render(request, 'views.py')

@login_required()
def unix(request):

    if request.GET:
        unixCommand = request.GET['unix']

        if re.search("\.\./", unixCommand):
            return HttpResponse(f"You are not allowed to back out of a folder. Sorry.")


        if unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "ls" or unixCommand == "ls -a" or unixCommand.startswith('ls'):
            words = unixCommand.split(' ')
            if re.search('-', unixCommand):
                words.insert(2, 'whiteBoxHacking/')
            else:
                words.insert(1, 'whiteBoxHacking/')
            newUnixCommand = ''
            for word in words:
                newUnixCommand += word
                if not word.endswith('/'):
                    newUnixCommand += ' '
            result = subprocess.run([newUnixCommand], stdout=subprocess.PIPE, shell=True)
            return HttpResponse(f"{result.stdout.decode('utf-8')}")

        elif unixCommand.startswith("cat"):
            if (unixCommand == 'cat .env'):
                challenge7 = Challenge.objects.get(templateValue=7)
                return HttpResponse(f"Challenge 7 Flag: {challenge7.flag}")

            words = unixCommand.split(' ')
            words.insert(1, 'whiteBoxHacking/')
            newUnixCommand = ''
            for word in words:
                newUnixCommand += word
                if not word.endswith('/'):
                    newUnixCommand += ' '

            result = subprocess.run([newUnixCommand], stdout=subprocess.PIPE, shell=True)
            return HttpResponse(f"{result.stdout.decode('utf-8')}")
        elif unixCommand.startswith("cp") or unixCommand.startswith("mv") or unixCommand.startswith("touch") or unixCommand.startswith("rm") or unixCommand.startswith("locate") or unixCommand.startswith("grep") or unixCommand.startswith("cd"):
            return HttpResponse("bash: "": command not found")
        else:
            return HttpResponse(f"bash: {unixCommand} not a valid command")

@login_required()
def cookieValidation(request):
    challenge = Challenge.objects.get(templateValue=9)
    if request.COOKIES.get('FORSPARTA!') == "HYAAAAAA!HYAAAAAA!HYAAAAAA!":
        return HttpResponse(challenge.flag)
    else:
        return HttpResponse("Not Authorized")


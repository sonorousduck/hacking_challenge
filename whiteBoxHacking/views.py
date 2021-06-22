from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess
import re


def index(request):
    return render(request, 'whiteBoxHacking/index.html')

def showViews(request):
    return render(request, 'views.py')

def unix(request):
   # Sadly, os.system wasn't working. It always returned a 0 or some number, I think most likely it knows what this is and it is trying to save me..? Maybe. I will hardcode it for now, probably safer anyways. 

    #test = os.system(request.GET['unix'])
    #newTest = str(test)


    #return HttpResponse(f"{newTest}", content_type='text/plain')

    if request.GET:
        unixCommand = request.GET['unix']

        # Got to do some scrubbing to allow for complete access of this folder, but none outside of it. Essentially, I need to limit the number of ../ allowed. Also, you always start in the base folder since os is running on the base folder, so I need to always move into the folder.





        if unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "ls" or unixCommand == "ls -a":
            unixCommand += " whiteBoxHacking/"
            result = subprocess.run([unixCommand], stdout=subprocess.PIPE, shell=True)
            return HttpResponse(f"files: {result.stdout}")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")
        elif unixCommand == "":
            return HttpResponse("bash: "": command not found")




# TODO: This will be good for the chroot jail thing. This allows a user to create a file from a command line.

#        elif unixCommand.startswith("touch"):
 #           print(unixCommand)
  #          words = unixCommand.split(' ')
   #         print(words)
    #        words.insert(1, 'whiteBoxHacking/')
     #       newUnix = ''
      #      for word in words:
       #         newUnix += word
        #        if not word.endswith('/'):
         #           newUnix += ' '
          #  print(newUnix)
#
 #           result = subprocess.run([newUnix], stdout=subprocess.PIPE, shell=True)
            
#            return HttpResponse("bash: "": command not found")

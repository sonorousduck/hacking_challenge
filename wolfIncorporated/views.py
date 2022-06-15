from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LoneWolfUser, FellowEmployee, Email
from loginSignup.models import CustomUser
from challenges.models import Challenge
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
import random
import json
from django.contrib import messages
from django.contrib.messages import get_messages


# Create your views here.

@login_required()
def index(request):
    try:
        if LoneWolfUser.objects.get(user=request.user).isServerDeleted:
            return HttpResponseRedirect("/LoneWolf/deleted")
    except:
        pass
        


    try:
        user = LoneWolfUser.objects.get(user=request.user)
        return HttpResponseRedirect('./homepage')
    except:
        if (request.GET):
            if ('EmployeeID' not in request.GET):

                try:
                    user = LoneWolfUser.objects.get(user=request.user)
                    return HttpResponseRedirect('./homepage')
                except:


                    loneWolfAgent = LoneWolfUser(serverIsRunning="False", username=request.GET['username'], user=request.user,  last_name=request.user.last_name)

                    loneWolfAgent.save()


                    # Create Fellow Employees

                    firstNames = ['John', 'Cortana', 'Jeff', 'Taylor', 'David', 'Erik', 'Ryan', 'Arthur', 'Steven', 'Cayde', 'Claire', 'Sophia', 'Abby', 'Emily', 'Eris', 'Luke', 'Anakin', 'Aang', 'Itadori', 'Tanjiro', 'Nezuko', 'Katara', 'Doom', 'Stewie', 'Doctor']
                    lastNames = ['Smith', 'Anderson', 'Six', 'Skywalker', 'Morn', 'Bray', 'Woodward', 'Gardner', 'Holliday', 'Williams', 'Hamill', 'Jarvis', 'Strange', 'Dixon', 'Skywalker', 'Kenobi', 'Stark', 'Wayne', 'Banner', 'Morgan', 'Mir', 'Guy', 'Baggins', 'AKA Batman', 'Griffin', 'Bond']

                    random.shuffle(firstNames)
                    random.shuffle(lastNames)
                    

                    for i in range(12):
                        fellowEmployee = FellowEmployee(username=f"{firstNames[i]}-{lastNames[i]}", loneWolfUser=loneWolfAgent, first_name=firstNames[i], last_name=lastNames[i], cookie=f"AA77{firstNames[i]}&*(FDSIJFSD?__){lastNames[i]}")
                        fellowEmployee.save()

                    adminEmployee = FellowEmployee(admin=True, username="Sauron", loneWolfUser=loneWolfAgent, first_name="Sauron", last_name="The Conquerer", cookie="dOn$eRiAngToRuleTD%7h@emAllSaur*onRu-les")
                    adminEmployee.save()

                    initialEmail = Email(loneWolfUser=loneWolfAgent, content=f'Welcome to Lone Wolf, {request.user.first_name}! Our Dev team just barely enabled support for limited script tags to work through email! Check it out! <div onmouseover=alert(\"Yay!\")> We are glad to have you! </div>',  sender=f"{adminEmployee.first_name} {adminEmployee.last_name}", subjectLine="Welcome to the company!", image='images/sauron.jpeg')
                    initialEmail.save()
                    

                    return HttpResponseRedirect('./homepage')

        return(render(request, 'wolfIncorporated/index.html'))

@login_required
def homepage(request):
    
    if LoneWolfUser.objects.get(user=request.user).isServerDeleted:
        return HttpResponseRedirect("/LoneWolf/deleted")


    try:
        employees = FellowEmployee.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user))[:7]
        emails = reversed(Email.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user)))
        everyone = FellowEmployee.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user))
        serverRunning = LoneWolfUser.objects.get(user=request.user).serverIsRunning
        cookieMessage = ''
        flag = Challenge.objects.get(templateValue=14).flag
        if get_messages(request):
            for message in get_messages(request):
                cookieMessage += str(message) + '\n'

        if request.COOKIES.get('Employee'):
            try:
                employee = FellowEmployee.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user)).get(cookie=request.COOKIES.get('Employee'))
                admin = employee.admin
                first_name = employee.first_name
                last_name = employee.last_name
                if admin:
                    flag = Challenge.objects.get(templateValue=14).flag
                else:
                    flag = Challenge.objects.get(templateValue=16).flag
                return render(request, 'wolfIncorporated/homepage.html', {'admin': admin, 'first_name': first_name, 'last_name': last_name, 'employees': employees, 'everyone': everyone, 'emails': emails, 'cookie': cookieMessage, 'serverRunning': serverRunning, 'flag': flag}) 
            except:
                return (render(request, 'wolfIncorporated/homepage.html', {'first_name': request.user.first_name, 'last_name': request.user.last_name, 'employees': employees, 'everyone': everyone, 'emails': emails, 'cookie': cookieMessage, 'serverRunning': serverRunning, 'flag': flag}))

        
        return (render(request, 'wolfIncorporated/homepage.html', {'first_name': request.user.first_name, 'last_name': request.user.last_name, 'employees': employees, 'everyone': everyone, 'emails': emails, 'cookie': cookieMessage, 'serverRunning': serverRunning, 'flag': flag}))

    except (Exception) as e:
        return HttpResponseRedirect('/LoneWolf')




@login_required()
def sendEmail(request):

    if LoneWolfUser.objects.get(user=request.user).isServerDeleted:
        return HttpResponseRedirect("/LoneWolf/deleted")

    if (request.POST):
        recipient = request.POST['recipient']
        subjectLine = request.POST['subjectLine']
        emailContent = request.POST['emailContent']

        cookieGetterPossibilities = ['onmouseover', 'onclick', 'onmousedown', 'ondblclick', 'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseup']


        if '<script>' in emailContent and '</script>' not in emailContent:
            emailContent += '</script> Whoops! You forgot to close your script tag! (We fixed it for you)'


        email = Email(loneWolfUser=LoneWolfUser.objects.get(user=request.user), content=emailContent, sender=f"To: {recipient}", subjectLine=subjectLine)
        email.save()

        while Email.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user)).count() > 5:
            Email.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user)).first().delete()

        
        if 'document.cookie' in emailContent:
            any_in = lambda a, b: bool(set(emailContent).intersection(cookieGetterPossibilities))
            if '<script>' in emailContent and '</script>' in emailContent or any_in:
                if 'fetch' in emailContent and '203.0.113.113' in emailContent and LoneWolfUser.objects.get(user=request.user).serverIsRunning:
                    if 'Everyone' == recipient:
                        employees = FellowEmployee.objects.filter(loneWolfUser = LoneWolfUser.objects.get(user=request.user))
                        cookieString = ''
                        for employee in employees:
                            cookieString += employee.cookie + '\n'
                        messages.add_message(request, messages.INFO, cookieString)
                        return HttpResponseRedirect(reverse('wolfIncorporated:Employee-Home-Page'))
                    else:
                        first = recipient.split(' ')
                        employee = FellowEmployee.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user)).get(first_name=first[0])
                        messages.add_message(request, messages.INFO, employee.cookie)
                        return HttpResponseRedirect(reverse('wolfIncorporated:Employee-Home-Page'))
                

    return HttpResponseRedirect(reverse('wolfIncorporated:Employee-Home-Page'))

@login_required()
def admin(request):
    if LoneWolfUser.objects.get(user=request.user).isServerDeleted:
        return HttpResponseRedirect("/LoneWolf/deleted")


    if request.COOKIES.get('Employee') != FellowEmployee.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user)).get(first_name="Sauron").cookie:
        return HttpResponseForbidden() 

    return render(request, 'wolfIncorporated/admin.html')


@login_required()
def deleteAllEmails(request):
    loneWolf = LoneWolfUser.objects.get(user=request.user)

    while Email.objects.filter(loneWolfUser=loneWolf).count() > 0:
        Email.objects.filter(loneWolfUser=loneWolf).first().delete()

    adminEmployee = FellowEmployee.objects.filter(loneWolfUser=loneWolf).get(admin=True)
    initialEmail = Email(loneWolfUser=loneWolf, content=f'Welcome to Lone Wolf, {request.user.first_name}! Our Dev team just barely enabled support for limited script tags to work through email! Check it out! <div onmouseover=alert(\"Yay!\")> We are glad to have you! </div>',  sender=f"{adminEmployee.first_name} {adminEmployee.last_name}", subjectLine="Welcome to the company!", image='images/sauron.jpeg')
    initialEmail.save()

    return HttpResponseRedirect(reverse('wolfIncorporated:Employee-Home-Page'))

@login_required()
def deleteServer(request):
    loneWolfAgent = LoneWolfUser.objects.get(user=request.user)
    
    if LoneWolfUser.objects.get(user=request.user).isServerDeleted:
        return HttpResponseRedirect("/LoneWolf/deleted")


    if request.COOKIES.get('Employee') != FellowEmployee.objects.filter(loneWolfUser=loneWolfAgent).get(first_name="Sauron").cookie:
        return HttpResponseForbidden() 

    loneWolfAgent.isServerDeleted = True 
    loneWolfAgent.save()

    Email.objects.filter(loneWolfUser=loneWolfAgent).delete()
    FellowEmployee.objects.filter(loneWolfUser=loneWolfAgent).delete()


    return HttpResponseRedirect(reverse('wolfIncorporated:deletedServer'))

@login_required()
def deletedServer(request):
    flag = Challenge.objects.get(templateValue=17).flag
    user = request.user

    customUser = CustomUser.objects.get(user=user)
    try:
        loneWolfUser = LoneWolfUser.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('wolfIncorporated:LoneWolf'))

    if (loneWolfUser.isServerDeleted):
        data = json.loads(customUser.challenges)
        challenges = Challenge.objects.filter(challengeSeries='LoneWolf')
        challenges = challenges[:len(challenges) - 1] # We don't want to auto complete the last challenge
        challengesToFinish = []
        for challenge in challenges:
            challengesToFinish.append(challenge.order)
        
        challengeCompletedCount = 0
        
        for number in challengesToFinish:
            if data[number]['completed'] != 'true':
                data[number]['completed'] = 'true'
                data[number]['hidden'] = 'false'
                data[number + 1]['hidden'] = 'false'
                challengeCompletedCount += 1

        customUser.challenges = json.dumps(data)
        customUser.completedChallenges += challengeCompletedCount
        customUser.correctInARow += challengeCompletedCount
        customUser.save()

        return render(request, 'wolfIncorporated/deletedServer.html', {'flag': flag})
    else:
        return HttpResponseRedirect(reverse('wolfIncorporated:Employee-Home-Page'))


@login_required()
def console(request):
    if not request.POST:
        if get_messages(request):
            messagesList = ''
            for message in get_messages(request):
                messagesList += str(message) +'\t'
            return render(request, 'wolfIncorporated/console.html', {'messages': messagesList})
        return render(request, 'wolfIncorporated/console.html')

    else:

        validCommands = ['python', 'ls', 'pwd', 'cat']
        files = 'server.py randomFile.txt anotherRandomFile.txt instructions.txt'
        instructions = "File Content: Start the server, and maybe try doing something to send a way to log in to the server? Just an idea...?"
        randomFile = "File Content: These are not the droids you are looking for" 
        anotherRandomFile = "File Content: Fetch! 'Good dog!', I proclaim, as the dog brings back the toy."
        server = """
                if __name__ == '__main__':
                    server_address = ('localhost', 8000)
                    print(f'Serving from http://{server_address[0]}:{server_address[1]}')
                    print('Press Ctrl-C to quit\n')
                    try:
                        HTTPServer(server_address, hacking_challenge).serve_forever()
                    except KeyboardInterrupt:
                        print('Exiting')
                        exit(0)
                """
        command = request.POST['console']
        commandList = list(filter(command.startswith, validCommands))
        try:
            isValidCommand = commandList[0] in validCommands 
        except:
            isValidCommand = False

        if isValidCommand:
            if commandList[0] == 'python':
                if command.endswith('server.py'):
                    loneWolfAgent = LoneWolfUser.objects.get(user=request.user)
                    
                    if loneWolfAgent.serverIsRunning:
                        messages.add_message(request, messages.INFO, "I don't understand... The server is already running on 203.0.113.113")
                    else:
                        loneWolfAgent.serverIsRunning = True
                        loneWolfAgent.save()
                        messages.add_message(request, messages.INFO, "Server Starting up... \n Server Running on 203.0.113.113. (Feel Free to write emails fetching to this server. It isn't a real one, just an emulated one)")



            elif commandList[0] == 'ls':
                messages.add_message(request, messages.INFO, files)
            elif commandList[0] == 'cat':
                if command.endswith('randomFile.txt'):
                    messages.add_message(request, messages.INFO, randomFile)
                elif command.endswith('anotherRandomFile.txt'):
                    messages.add_message(request, messages.INFO, anotherRandomFile)
                elif command.endswith('instructions.txt'):
                    messages.add_message(request, messages.INFO, instructions)
                elif command.endswith('server.py'):
                    messages.add_message(request, messages.INFO, server)
        else:
            messages.add_message(request, messages.INFO, "Invalid Command") 
        
        return HttpResponseRedirect(reverse('wolfIncorporated:console'), request)












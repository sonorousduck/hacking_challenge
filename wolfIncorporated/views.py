from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LoneWolfUser, FellowEmployee, Email
from django.http import HttpResponseRedirect
import random

# Create your views here.


#TODO: Somehow redirect here if they don't have a Lone Wolf Account. Else go to home page of Lone Wolf

@login_required()
def index(request):
        
    try:
        user = LoneWolfUser.objects.get(user=request.user)
        return HttpResponseRedirect('./homepage')
    except:
        if (request.GET):
            if ('EmployeeID' not in request.GET):
                print(f"Welcome {request.GET['username']}")
                print("Create user, create database stuff, and everything. Instantiate to non-admin")

                try:
                    user = LoneWolfUser.objects.get(user=request.user)
                    return HttpResponseRedirect('./homepage')
                except:


                    loneWolfAgent = LoneWolfUser(admin="False", username=request.GET['username'], user=request.user,  last_name=request.user.last_name)

                    loneWolfAgent.save()


                    # Create Fellow Employees

                    firstNames = ['John', 'Cortana', 'Jeff', 'Taylor', 'David', 'Erik', 'Ryan', 'Arthur', 'Steven', 'Cayde', 'Claire', 'Sophia', 'Abby', 'Emily', 'Eris', 'Luke', 'Anakin', 'Aang', 'Itadori', 'Tanjiro', 'Nezuko', 'Katara', 'Doom', 'Stewie', 'James']
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
    try:
        employees = FellowEmployee.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user))[:7]
        emails = Email.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user))[:7]
        everyone = FellowEmployee.objects.filter(loneWolfUser=LoneWolfUser.objects.get(user=request.user))
        if request.COOKIES.get('Employee'):
            print("Got Here")
            try:
                employee = FellowEmployee.objects.get(cookie=request.COOKIES.get('Employee'))
                admin = employee.admin
                first_name = employee.first_name
                last_name = employee.last_name
                return render(request, 'wolfIncorporated/homepage.html', {'admin': admin, 'first_name': first_name, 'last_name': last_name, 'employees': employees, 'everyone': everyone, 'emails': emails}) 
            except:
                return (render(request, 'wolfIncorporated/homepage.html', {'first_name': request.user.first_name, 'last_name': request.user.last_name, 'employees': employees, 'everyone': everyone, 'emails': emails}))

        return (render(request, 'wolfIncorporated/homepage.html', {'first_name': request.user.first_name, 'last_name': request.user.last_name, 'employees': employees, 'everyone': everyone, 'emails': emails}))

    except (Exception) as e:
        print(e)
        return HttpResponseRedirect('/LoneWolf')






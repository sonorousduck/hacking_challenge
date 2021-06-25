from django.shortcuts import render

# Create your views here.


def userSpecificIndex(request, username):
    print(username)
    return render(request, 'chroot/index.html')

"""hacking_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


# TODO: seperate out security and cookieValidation into its own apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenges/', include('challenges.urls')),
    path('playground/', include('playground.urls')),
    path('', include('homepage.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('security/', include('challenges.urls')),
    path('login/', include('loginSignup.urls')),
    path('settings/', include('settings.urls')),
    path('LoneWolf/', include('wolfIncorporated.urls')),
    path('WhiteBox/', include('whiteBoxHacking.urls')),


    ]

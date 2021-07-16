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
    path('login/', include('loginSignup.urls')),
    path('settings/', include('settings.urls')),
    path('LoneWolf/', include('wolfIncorporated.urls')),
    path('WhiteBox/', include('whiteBoxHacking.urls')),
    path('Phenomenal.png', RedirectView.as_view(url=staticfiles_storage.url('Phenomenal.png'))),
    path('2Down.PNG', RedirectView.as_view(url=staticfiles_storage.url('2Down.PNG'))),
    path('3Down.PNG', RedirectView.as_view(url=staticfiles_storage.url('3Down.PNG'))),
    path('Ascended.PNG', RedirectView.as_view(url=staticfiles_storage.url('Ascended.PNG'))),
    path('Breathtaking.PNG', RedirectView.as_view(url=staticfiles_storage.url('Breathtaking.PNG'))),
    path('ClassFirst.PNG', RedirectView.as_view(url=staticfiles_storage.url('ClassFirst.PNG'))),
    path('ClassSecond.PNG', RedirectView.as_view(url=staticfiles_storage.url('ClassSecond.PNG'))),
    path('ClassThird.PNG', RedirectView.as_view(url=staticfiles_storage.url('ClassThird.PNG'))),
    path('Completion.PNG', RedirectView.as_view(url=staticfiles_storage.url('Completion.PNG'))),
    path('DeadEye.PNG', RedirectView.as_view(url=staticfiles_storage.url('DeadEye.PNG'))),
    path('Flawless.PNG', RedirectView.as_view(url=staticfiles_storage.url('Flawless.PNG'))),
    path('GoldenEye.PNG', RedirectView.as_view(url=staticfiles_storage.url('GoldenEye.PNG'))),
    path('PlayingWithFire.PNG', RedirectView.as_view(url=staticfiles_storage.url('PlayingWithFire.PNG'))),
    path('Tenacious.PNG', RedirectView.as_view(url=staticfiles_storage.url('Tenacious.PNG'))),
    path('Committed.PNG', RedirectView.as_view(url=staticfiles_storage.url('Committed.PNG'))),
    path('BotStatus.PNG', RedirectView.as_view(url=staticfiles_storage.url('BotStatus.PNG'))),
    path('UOKBro.PNG', RedirectView.as_view(url=staticfiles_storage.url('UOKBro.PNG'))),
    path('Unstoppable.PNG', RedirectView.as_view(url=staticfiles_storage.url('Unstoppable.PNG'))),
    path('Unforgettable.PNG', RedirectView.as_view(url=staticfiles_storage.url('Unforgettable.PNG'))),
    path('EarlyBird.PNG', RedirectView.as_view(url=staticfiles_storage.url('EarlyBird.PNG'))),
    path('chroot/', include('chroot.urls')),
    path('customAdmin/', include('customAdmin.urls')),
    ]

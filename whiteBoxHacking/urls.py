from django.urls import path

from . import views

app_name='whiteBoxHacking'

# Remember everyone! The password for the 8th challenge is {}
urlpatterns = [
        path('', views.index, name='whiteBox'),
        path('views.py/', views.showViews, name='views'),
        path('giveWhatTheyWant', views.unix, name='unix'),
        path('cookieValidation', views.cookieValidation, name='cookieValidation'),
]

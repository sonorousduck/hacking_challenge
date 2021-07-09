from django.urls import path

from . import views

app_name='whiteBoxHacking'

urlpatterns = [
        path('', views.index, name='whiteBox'),
        path('views.py/', views.showViews, name='views'),
        path('giveWhatTheyWant', views.unix, name='unix'),


]

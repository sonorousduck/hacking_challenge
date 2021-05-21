from django.urls import path

from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('getChallenges/', views.getChallenges, name='getChallenges'),


]

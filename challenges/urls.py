from django.urls import path

from . import views

app_name='challenges'


urlpatterns = [
        path('', views.index, name='challenges'),
        path('getChallenges', views.getChallenges, name='getChallenges'),
        path('<int:challenge_id>/', views.challengeDetails, name='challengeDetails'),

]

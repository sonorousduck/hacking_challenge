from . import views
from django.urls import path

app_name='homepage'


urlpatterns = [
        path('', views.index, name='index'),
        path('logoutUser', views.logoutUser, name='logout'),
        path('resetFlavorText', views.resetFlavorText, name='resetFlavorText'),


        ]




        

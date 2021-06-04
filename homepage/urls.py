from . import views
from django.urls import path

urlpatterns = [
        path('', views.index, name='index'),
        path('logoutUser', views.logoutUser, name='logout'),
        path('resetFlavorText', views.resetFlavorText, name='resetFlavorText'),


        ]




        

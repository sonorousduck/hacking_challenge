from django.urls import path

from . import views


app_name ='loginSignup'

urlpatterns = [
        path('', views.index, name='login'),
        path('signUp', views.signUp, name='signUp'),
        path('signIn', views.signIn, name='signIn'),

]

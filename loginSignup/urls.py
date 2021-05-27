from django.urls import path

from . import views


app_name ='loginSignup'

urlpatterns = [
        path('', views.index, name='login'),
        path('signUp', views.signUp, name='signUp'),
        path('createAccount/', views.createAccount, name='createAccount')
]

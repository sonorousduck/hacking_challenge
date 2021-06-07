from django.urls import path
from . import views

app_name = "wolfIncorporated"

urlpatterns = [
        path('', views.index, name='Lone Wolf'),
        path('homepage/', views.homepage, name='Employee Home Page'),

        ]

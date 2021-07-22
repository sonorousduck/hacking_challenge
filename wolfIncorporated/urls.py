from django.urls import path
from . import views

app_name = "wolfIncorporated"

urlpatterns = [
        path('', views.index, name='LoneWolf'),
        path('homepage/', views.homepage, name='Employee-Home-Page'),
        path('sendEmail/', views.sendEmail, name='Send Email'),
        path('homepage/admin/', views.admin, name="admin"),
        path('homepage/admin/deleteServer/', views.deleteServer, name="deleteServer"),
        path('deleted', views.deletedServer, name="deletedServer"),
        path('homepage/console/', views.console, name='console'),
        path('homepage/deleteEmails/', views.deleteAllEmails, name='deleteEmails'),
        ]

from django.urls import path
from . import views

app_name = "settings"

urlpatterns = [
        path('', views.index, name="settings"),
        path('updateText', views.updateText, name='updateText'),
        path('updatePassword', views.updatePassword, name='updatePassword'),
        ]


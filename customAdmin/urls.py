from django.urls import path

from . import views

app_name = "customAdmin"

urlpatterns = [
        path('', views.index, name='index'),
        path('changeDate/', views.changeDate, name='changeDate'),
        path('shuffle/', views.mix_flags, name='shuffle'),
        ]

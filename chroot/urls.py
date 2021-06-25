from django.urls import path

from . import views

app_name='chroot'

urlpatterns = [
        path('<username>/', views.userSpecificIndex, name='userSpecificIndex'),

    ]

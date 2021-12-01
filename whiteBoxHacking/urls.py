from django.urls import path

from . import views

app_name='whiteBoxHacking'

# Remember everyone! The password for the 8th challenge is 1a2s3d4f5g6h7j8k9l
urlpatterns = [
        path('', views.index, name='whiteBox'),
        path('views.py/', views.showViews, name='views'),
        path('giveWhatTheyWant', views.unix, name='unix'),
        path('cookieValidation', views.cookieValidation, name='cookieValidation'),
]

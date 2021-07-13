from django.urls import path

from . import views

app_name='challenges'


urlpatterns = [
        path('', views.index, name='challenges'),
        path('<int:order>/', views.challengeDetails, name='challengeDetails'),
        path('validation/', views.validation, name='validation'),
        path('passwordSecurity', views.passwordSecurity, name='passwordSecurity'),
        path('supersecure', views.security, name='supersecure'),
        path('securityValidation', views.securityValidation, name='securityValidation'),
        path('secure', views.secure, name='secure'),
        path('cookieValidation/', views.cookieValidation, name='cookieValidation'),
        path('adminLogin/', views.adminLogin, name='adminLogin'),
        path('completed/', views.completed, name='completed'),
        path('allChallenges/', views.allChallenges, name='allChallenges'),
]

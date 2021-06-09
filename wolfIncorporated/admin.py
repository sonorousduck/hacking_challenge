from django.contrib import admin
from .models import LoneWolfUser, FellowEmployee, Email
# Register your models here.

admin.site.register(LoneWolfUser)
admin.site.register(FellowEmployee)
admin.site.register(Email)

from django.contrib import admin
from .models import CustomUser
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .resources import CustomUserAdmin

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models import CustomUser
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CustomUserResource(resources.ModelResource):


    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name', 'completedChallenges', 'numChallenges')
        export_order = ('last_name', 'first_name', 'completedChallenges', 'numChallenges')

class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource


admin.site.register(CustomUser, CustomUserAdmin)

from .models import CustomUser
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CustomUserResource(resources.ModelResource):


    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name', 'percentComplete', 'completedChallenges', 'numRequiredChallenges', 'numChallenges')
        export_order = ('last_name', 'first_name', 'percentComplete', 'completedChallenges', 'numRequiredChallenges', 'numChallenges')

class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource

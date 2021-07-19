from django.core.management.base import BaseCommand, CommandError
from loginSignup.resources import CustomUserResource 

class Command(BaseCommand):
    help = "Used to get a list of all people and their scores"

    def handle(self, *args, **options):
        custom_user_resource = CustomUserResource()
        dataset = custom_user_resource.export()
        return dataset.csv



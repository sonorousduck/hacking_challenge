from django.db import models

# Create your models here.

class Testing(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateField()
    completed = models.BooleanField()






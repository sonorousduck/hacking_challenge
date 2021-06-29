from django.db import models
from datetime import datetime

# Create your models here.

class AssignmentDates(models.Model):
    date = models.DateField(default=datetime.today, blank=True)
    time = models.TimeField(default=datetime.utcnow, blank=True)
    description = models.CharField(max_length=30, default="open")


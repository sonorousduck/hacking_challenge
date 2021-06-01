from django.db import models
from challenges.models import Challenge
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(models.Model):
    numChallenges = models.IntegerField(default=0)
    completedChallenges = models.IntegerField(default=0)
    challenges = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)


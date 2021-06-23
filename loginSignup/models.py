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
    last_name = models.TextField(default="")
    customText = models.TextField(default="")
    numTotalIncorrectGuesses = models.IntegerField(default=0)
    incorrectPerChallenge = models.JSONField()


    class Meta:
        ordering = ['last_name']




    def __str__(self):
        return f" {self.user.first_name} {self.user.last_name} { round(((self.completedChallenges / self.numChallenges) * 100), 2) }%"

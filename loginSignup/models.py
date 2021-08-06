from django.db import models
from challenges.models import Challenge
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(models.Model):
    numChallenges = models.IntegerField(default=0)
    numRequiredChallenges = models.IntegerField(default=0)
    completedChallenges = models.IntegerField(default=0)
    completedRequiredChallenges = models.IntegerField(default=0)
    challenges = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    customText = models.TextField(default="", blank=True)
    numTotalIncorrectGuesses = models.IntegerField(default=0)
    incorrectPerChallenge = models.JSONField()
    achievements = models.JSONField()
    correctInARow = models.IntegerField(default=0)
    completedAllChallenges = models.BooleanField(default=False)
    percentComplete = models.FloatField(default=0.00)

    class Meta:
        ordering = ['last_name']




    def __str__(self):
        return f" {self.user.first_name} {self.user.last_name} { round(((self.completedRequiredChallenges / self.numRequiredChallenges) * 100), 2) }%"




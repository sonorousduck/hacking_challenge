from django.db import models


class Challenge(models.Model):
    flag = models.CharField(max_length=50)
    title = models.CharField(max_length=20, default='Challenge')
    description = models.CharField(max_length=300, default='A very nice description')
    order = models.IntegerField()
    templateValue = models.IntegerField(default=-1)
    hidden = models.BooleanField(default=False)
    pointValue = models.IntegerField(default=10)
    optionalChallenge = models.BooleanField(default=False)
    difficultyIndicator = models.CharField(max_length=20, default='Easy')
    challengeSeries = models.CharField(max_length=50, default="Basic")
    totalIncorrectGuesses = models.IntegerField(default=0)
    numberOfUsersOnThisChallenge = models.IntegerField(default=0)


    class Meta:
        ordering = ['order']


    def __str__(self):
        return str(f'Challenge {self.order}')



# Having hint seperate will allow easier adding of new hints to each specific challenge

class Hint(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    hint = models.TextField()


    def __str__(self):
        return str(self.challenge.title)



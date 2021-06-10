from django.db import models

# Create your models here.


# This is my thought on this model. We will have a challenge "model" that basically holds all the base information that a challenge may or may not need. We will also have another app called "User" that will contain if the challenge is completed or not for them. This may prove to be tricky, as the user model will then depend on the challenges model. I'm almost 100% certain that kind of thing exists, it will just be research

class Challenge(models.Model):
    flag = models.CharField(max_length=50)
    title = models.CharField(max_length=20, default='Level')
    description = models.CharField(max_length=300, default='A very nice description')
    order = models.IntegerField()
    hidden = models.BooleanField(default=False)
    pointValue = models.IntegerField(default=10)
    optionalChallenge = models.BooleanField(default=False)
    difficultyIndicator = models.CharField(max_length=20, default='Easy')
    challengeSeries = models.CharField(max_length=50, default="Basic")



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



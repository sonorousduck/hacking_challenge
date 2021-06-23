from django.db import models

class Achievements(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    achievementIcon = models.ImageField()
    


    def __str__(self):
        return f"{self.title}"



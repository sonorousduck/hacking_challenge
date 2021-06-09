from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class LoneWolfUser(models.Model):
    admin = models.BooleanField(default=False)
    username = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isServerDeleted = models.BooleanField(default=False)
    last_name = models.TextField(default="")


    class Meta:
        ordering = ['last_name']



    def __str__(self):
        return f" {self.user.first_name} {self.user.last_name} Is an admin: {self.admin} and has destroyed the company? {self.isServerDeleted}"




class FellowEmployee(models.Model):
    admin = models.BooleanField(default=False)
    username = models.CharField(max_length=30)
    loneWolfUser = models.ForeignKey(LoneWolfUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cookie = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.loneWolfUser.user.first_name} {self.loneWolfUser.user.last_name}: {self.first_name} {self.last_name}"

class Email(models.Model):
    loneWolfUser = models.ForeignKey(LoneWolfUser, on_delete=models.CASCADE)
    content = models.TextField(default="")
    sender = models.CharField(max_length=30)
    image = models.ImageField()
    subjectLine = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.loneWolfUser.user.first_name} {self.loneWolfUser.user.last_name} email #{Email.objects.all().count()}"






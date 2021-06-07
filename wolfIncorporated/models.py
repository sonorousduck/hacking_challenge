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

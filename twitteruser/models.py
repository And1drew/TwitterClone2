from django.contrib.auth.models import AbstractUser
from django.db import models
from twitterclone import settings
# Create your models here.


class custom_user(AbstractUser):
    displayname = models.CharField(max_length = 60) 
    email = models.CharField(max_length = 120)
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    
    def __str__(self):
        return self.displayname
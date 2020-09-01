from django.db import models
from twitteruser.models import custom_user
# Create your models here.


class tweet_model(models.Model):
    text = models.CharField(max_length=140)
    author = models.ForeignKey(custom_user, on_delete=models.CASCADE)

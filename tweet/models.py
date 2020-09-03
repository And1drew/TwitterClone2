from django.db import models
from django.utils import timezone
from datetime import datetime
from twitteruser.models import TwitterUser
# Create your models here.


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.text

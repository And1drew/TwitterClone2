from django.db import models
from datetime import datetime
from twitteruser.models import custom_user
# Create your models here.


class tweet_model(models.Model):
    text = models.CharField(max_length=140)
    author = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return self.text

from django.db import models
from twitteruser.models import TwitterUser

# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=140)
    alert_for = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    created_by = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='creator', default='')
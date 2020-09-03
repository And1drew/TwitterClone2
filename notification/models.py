from django.db import models
from twitteruser.models import custom_user

# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=140)
    alert_for = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    created_by = models.ForeignKey(custom_user, on_delete=models.CASCADE, related_name='creator', default='')
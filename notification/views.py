from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from notification.models import Notification
# Create your views here.

def notification_view(request):
    notifications = Notification.objects.filter(alert_for=request.user.id)
    return render(request, 'notifications.html',{'notifications': notifications})
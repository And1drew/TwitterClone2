from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from notification.models import Notification
# Create your views here.


@login_required
def notification_view(request):
    notifications = Notification.objects.filter(alert_for=request.user.id)
    return render(request, 'notifications.html',{'notifications': notifications})


@login_required
def mark_as_seen(request):
    Notification.objects.filter(alert_for=request.user.id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
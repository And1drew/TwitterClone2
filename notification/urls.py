from django.urls import path
from notification import views

urlpatterns = [
    path('seenotifications/', views.mark_as_seen),
    path('notifications/', views.notification_view),
]
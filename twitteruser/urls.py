from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup_view)
]

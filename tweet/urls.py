from django.urls import path
from tweet import views

urlpatterns = [
    path('tweet/<int:tweet_id>/', views.tweet_details),
    path('tweet/', views.new_tweet),
]
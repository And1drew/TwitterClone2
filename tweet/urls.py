from django.urls import path
from tweet import views

urlpatterns = [
    path('tweet/', views.new_tweet),
]
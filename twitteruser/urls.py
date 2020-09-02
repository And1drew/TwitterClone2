from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup_view),
    path('profile/', views.profile_view),
    path('user/<int:user_id>/', views.user_details),
    path('follow/<int:user_id>/', views.follow_view),
    path('unfollow/<int:user_id>/', views.unfollow_view),
]

from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('user/<int:user_id>/', views.UserDetailsView.as_view()),
    path('follow/<int:user_id>/', views.FollowView.as_view()),
    path('unfollow/<int:user_id>/', views.UnfollowView.as_view()),
]

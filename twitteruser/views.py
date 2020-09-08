from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification
from twitteruser.forms import signup_form


class IndexView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        tweets = Tweet.objects.order_by('-date')
        return render(request, 'index.html',{'tweets':tweets})


class SignUpView(TemplateView):

    def post(self, request):
        form = signup_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=form.get('username'),
                password=form.get('password'), 
                displayname=form.get('displayname'), 
                email=form.get('email'))
            return HttpResponseRedirect('/') 

    def get(self, request):
        form = signup_form()
        return render(request, 'signup_form.html', {'form': form})


class UserDetailsView(TemplateView):

    def get(self, request, user_id):
        user = TwitterUser.objects.get(id=user_id)
        users_tweets = Tweet.objects.all().order_by('-date')
        followers = TwitterUser.objects.filter(follower=user).values('follower').count()
        return render(request, 'user_details.html', {'user':user, 'tweets':users_tweets, 'followers':followers})


class ProfileView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        tweets = Tweet.objects.all().order_by('-date')
        my_tweets = Tweet.objects.filter(author=request.user).count()
        followers = TwitterUser.objects.filter(follower=request.user).values('follower').count()
        notifications = Notification.objects.filter(alert_for=request.user)
        return render(request, 'profile.html', {'tweets':tweets, 'followers':followers, 'notifications':notifications, 'mytweets':my_tweets})


class FollowView(LoginRequiredMixin, TemplateView):

    def get(self, request, user_id):
        user_to_follow = TwitterUser.objects.filter(id=user_id).first()
        request.user.follower.add(user_to_follow)
        request.user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


class UnfollowView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, user_id):
        user_to_unfollow = TwitterUser.objects.filter(id=user_id).first()
        request.user.follower.remove(user_to_unfollow)
        request.user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
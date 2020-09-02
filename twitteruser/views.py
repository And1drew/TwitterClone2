from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import custom_user
from tweet.models import tweet_model
from twitteruser.forms import signup_form

# Create your views here.
@login_required
def index(request):
    tweets = tweet_model.objects.order_by('-date')
    return render(request, 'index.html',{'tweets':tweets})


def signup_view(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_user = custom_user.objects.create_user(username=form.get('username'), password=form.get('password'), displayname=form.get('displayname'), email=form.get('email'))
            return HttpResponseRedirect('/')
    form = signup_form()
    return render(request, 'signup_form.html', {'form': form})


@login_required
def user_details(request, user_id):
    user = custom_user.objects.get(id=user_id)
    users_tweets = tweet_model.objects.all()
    followers = custom_user.objects.filter(follower=user).values('follower').count()
    return render(request, 'user_details.html', {'user':user, 'tweets':users_tweets, 'followers':followers})


@login_required
def profile_view(request):
    my_tweets = tweet_model.objects.all()
    followers = custom_user.objects.filter(follower=request.user).values('follower').count()
    return render(request, 'profile.html', {'tweets':my_tweets, 'followers':followers})


@login_required
def follow_view(request, user_id):
    user_to_follow = custom_user.objects.filter(id=user_id).first()
    request.user.follower.add(user_to_follow)
    request.user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


@login_required
def unfollow_view(request, user_id):
    user_to_unfollow = custom_user.objects.filter(id=user_id).first()
    request.user.follower.remove(user_to_unfollow)
    request.user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
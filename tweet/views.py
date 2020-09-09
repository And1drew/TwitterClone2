from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification
from tweet.forms import tweet_form
import re
# Create your views here.

@login_required
def new_tweet(request):
    if request.method == 'POST':
        form = tweet_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_tweet = Tweet.objects.create(
                text = form.get('text'),
                author = request.user
            )
            alerted_username = parse_tweet(new_tweet.text)
            if alerted_username:
                if TwitterUser.objects.filter(username=alerted_username).exists():
                    Notification.objects.create(
                        message = new_tweet.text,
                        alert_for = TwitterUser.objects.get(username=alerted_username),
                        created_by = request.user
                    )
                    return HttpResponseRedirect('/')
                else:
                    print('user not found')
                    return HttpResponseRedirect('/')
            else:
                print('user not found')
                return HttpResponseRedirect('/')
    form = tweet_form
    return render(request, 'tweet_form.html', {'form': form})


def parse_tweet(text):
    """helper function for pasrsing tweets and creating notifications"""
    username_match = re.search(r"@(\b\w+)\s", text)
    if username_match:
        username = username_match.group(1)
        return username



def tweet_details(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_details.html', {'tweet':tweet})
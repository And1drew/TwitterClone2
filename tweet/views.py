from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import custom_user
from tweet.models import tweet_model
from tweet.forms import tweet_form
# Create your views here.

@login_required
def new_tweet(request):
    if request.method == 'POST':
        form = tweet_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_tweet = tweet_model.objects.create(
                text = form.get('text'),
                author = request.user
            )
            return HttpResponseRedirect('/')
    form = tweet_form
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_details(request, tweet_id):
    tweet = tweet_model.objects.get(id=tweet_id)
    return render(request, 'tweet_details.html', {'tweet':tweet})
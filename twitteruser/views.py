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
    tweets = tweet_model.objects.all()
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

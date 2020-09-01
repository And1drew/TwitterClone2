from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from authentication.forms import login_form
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            user = authenticate(request, username=form.get('username'), password=form.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = login_form
    return render(request, 'login_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
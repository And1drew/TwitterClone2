from django import forms

class tweet_form(forms.Form):
    text = forms.CharField(max_length=140)
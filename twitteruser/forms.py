from twitteruser.models import TwitterUser
from django import forms

class signup_form(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields =['username', 'password', 'displayname', 'email']
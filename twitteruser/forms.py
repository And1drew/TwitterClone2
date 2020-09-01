from twitteruser.models import custom_user
from django import forms

class signup_form(forms.ModelForm):
    class Meta:
        model = custom_user
        fields =['username', 'password', 'displayname', 'email']
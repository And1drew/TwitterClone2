from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import custom_user
# Register your models here.


admin.site.register(custom_user, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser
# Register your models here.

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('displayname', 'follower')}),

admin.site.register(TwitterUser, UserAdmin)
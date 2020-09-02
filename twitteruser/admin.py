from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import custom_user
# Register your models here.

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('displayname', 'follower')}),

admin.site.register(custom_user, UserAdmin)
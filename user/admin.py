from django.contrib import admin

from user.models import Profile, User

admin.site.register([User, Profile])

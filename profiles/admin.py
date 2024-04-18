from django.contrib import admin
from .models import Profile, FriendRequest, SessionInvite

# Register your models here.
admin.site.register(Profile)
admin.site.register(FriendRequest)
admin.site.register(SessionInvite)
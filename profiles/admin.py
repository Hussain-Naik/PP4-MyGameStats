'''Admin for profile app'''
from django.contrib import admin
from .models import Profile, FriendRequest, SessionInvite


admin.site.register(Profile)
admin.site.register(FriendRequest)
admin.site.register(SessionInvite)

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(Session)
admin.site.register(Roster)
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Game)
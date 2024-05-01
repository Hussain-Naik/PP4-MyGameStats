from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', include('profiles.urls')),
    path('', include('home.urls')),
]

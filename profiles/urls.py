from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfileView.as_view(), name="profile"),
    path('<pk>/', views.UserProfileView.as_view(), name="user_profile"),
    path('update/', views.UpdateProfile.as_view(), name="update_profile"),
]
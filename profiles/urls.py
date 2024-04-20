from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfileView.as_view(), name="profile"),
    path('update/', views.UpdateProfile.as_view(), name="update_profile"),
    path('search/', views.FriendSearchView.as_view(), name="search_profile"),
    path('<pk>/', views.UserProfileView.as_view(), name="user_profile"),
    path('request/<pk>/update/', views.UpdateFriendRequestView.as_view(), name="update_request"),
]
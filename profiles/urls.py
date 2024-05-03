'''urls for profile app'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfileView.as_view(), name="profile"),
    path('update/', views.UpdateProfile.as_view(), name="update_profile"),
    path('search/', views.FriendSearchView.as_view(), name="search_profile"),
    path('<pk>/', views.UserProfileView.as_view(), name="user_profile"),
    path(
        '<pk>/remove/',
        views.RemoveFriendView.as_view(),
        name="unfriend"
        ),
    path(
        'request/search/',
        views.FriendRequestListView.as_view(),
        name="list_request"
        ),
    path(
        'request/<pk>/update/',
        views.UpdateFriendRequestView.as_view(),
        name="update_request"
        ),
    path(
        'request/<pk>/delete/',
        views.DeleteFriendRequestView.as_view(),
        name="delete_request"
        ),
    path(
        'session/search/',
        views.SessionRequestListView.as_view(),
        name="list_invites"
        ),
    path(
        'session/<pk>/update/',
        views.UserSessionInviteView.as_view(),
        name="update_invites"
        ),
    path(
        'session/<pk>/delete/',
        views.DeleteUserSessionInviteView.as_view(),
        name="delete_invites"
        ),
]

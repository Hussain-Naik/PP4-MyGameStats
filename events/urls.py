from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupListView.as_view(), name="groups"),
    path('groups/create/', views.CreateGroupView.as_view(), name="group_create"),
    path('groups/<pk>/', views.GroupDetailView.as_view(), name="group_detail"),
    path('groups/<pk>/update/', views.UpdateGroupView.as_view(), name="group_update"),
    path('groups/<pk>/delete/', views.DeleteGroup.as_view(), name="group_delete"),
    path('groups/<pk>/create/', views.CreateSessionView.as_view(), name="session_create"),
    path('session/<pk>/', views.SessionDetailView.as_view(), name="session"),
    path('session/<pk>/update/', views.UpdateSessionView.as_view(), name="session_update"),
    path('session/<pk>/delete/', views.DeleteSession.as_view(), name="session_delete"),
    path('session/game/<pk>/', views.GameDetailView.as_view(), name="game"),
    path('session/<pk>/invites/', views.SessionInviteView.as_view(), name="session_invite"),
    path('session/<pk>/invites/send/', views.CreateSessionInviteView.as_view(), name="send_invite"),
    path('session/<pk>/invites/delete/', views.DeleteSessionInvite.as_view(), name="delete_session_invite"),
    path('session/roster/delete/<pk>/', views.RosterPlayerRemoveView.as_view(), name="remove_player"),
]
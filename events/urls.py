from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupListView.as_view(), name="groups"),
    path('groups/create/', views.CreateGroupView.as_view(), name="group_create"),
    path('groups/<pk>/', views.GroupDetailView.as_view(), name="group_detail"),
    path('groups/<pk>/update/', views.UpdateGroupView.as_view(), name="group_update"),
    path('groups/<pk>/create/', views.CreateSessionView.as_view(), name="session_create"),
    path('session/<pk>/', views.SessionDetailView.as_view(), name="session"),
    path('session/<pk>/update/', views.UpdateSessionView.as_view(), name="session_update"),
    path('session/game/<pk>/', views.GameDetailView.as_view(), name="game"),
    path('session/<pk>/invites/send/', views.CreateSessionInviteView.as_view(), name="send_invite"),
]
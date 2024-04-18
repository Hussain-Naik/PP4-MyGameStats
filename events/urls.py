from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupListView.as_view(), name="groups"),
    path('groups/create/', views.CreateGroupView.as_view(), name="group_create"),
    path('groups/<pk>/', views.GroupDetailView.as_view(), name="group_detail"),
]
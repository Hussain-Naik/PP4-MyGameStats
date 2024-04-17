from django.contrib.auth.mixins import AccessMixin
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
class MyProfileView(LoginRequiredMixin, DetailView):
  model = User
  template_name = 'profiles/profile.html'
  context_object_name = 'user_object'

  def get_object(self):
    return get_object_or_404(User, id=self.request.user.id)
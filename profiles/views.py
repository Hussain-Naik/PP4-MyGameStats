from django.contrib.auth.mixins import AccessMixin
from django.views.generic.edit import CreateView, UpdateView, FormMixin, DeleteView
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
class MyProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profiles/profile.html'
    context_object_name = 'user_object'

    def get_object(self):
      return get_object_or_404(User, id=self.request.user.id)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'home/form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
      return get_object_or_404(User, id=self.request.user.id)
    
    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['page'] = 'User Update Form'
          return context
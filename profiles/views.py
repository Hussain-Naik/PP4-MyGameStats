from django.contrib.auth.mixins import AccessMixin
from django.views.generic.edit import CreateView, UpdateView, FormMixin, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
class MyProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'user_object'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = CustomUserChangeForm
    template_name = 'home/form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return get_object_or_404(Profile, user__id=self.request.user.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'User Update Form'
        return context

class UserProfileView(FormMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'user_object'
    form_class = FriendRequestForm

    def get_success_url(self):
        return reverse_lazy("user_profile", kwargs={"pk": self.kwargs['pk']})
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
      
    def form_valid(self, form):
        receiver_ = Profile.objects.get(id=self.kwargs['pk'])
        sender_ = Profile.objects.get(user__id=self.request.user.id)
        print(sender_, receiver_)
        FriendRequest.objects.get_or_create(sender=sender_, receiver=receiver_, status='pending')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and FriendRequest.objects.filter(
              sender= Profile.objects.get(user__id=self.request.user.id), 
              receiver=Profile.objects.get(id=self.kwargs['pk'])
          ).exists():
            context['sendRequest'] = FriendRequest.objects.get(
                sender= Profile.objects.get(user__id=self.request.user.id), 
                receiver=Profile.objects.get(id=self.kwargs['pk'])
          )
        else:
          context['sendRequest'] = False
        return context

class FriendSearchView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'list_object'
    paginate_by = 12


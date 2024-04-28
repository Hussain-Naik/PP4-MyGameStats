from django.contrib.auth.mixins import AccessMixin
from django.views.generic.edit import CreateView, UpdateView, FormMixin, DeleteView
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from .models import *


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

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET.get('q') != None else ''
        queryset = Profile.objects.filter(
            Q(first_name__icontains=q) | 
            Q(last_name__icontains=q) | 
            Q(user__username__icontains=q)
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        return context

class UpdateFriendRequestView(AccessMixin, UpdateView):
    model = FriendRequest
    
    template_name = 'home/form.html'
    success_url = reverse_lazy('profile')

    def get_form_class(self):
        form_class = UpdateFriendRequestForm
        if self.get_object().sender.user == self.request.user:
            form_class = UpdateFriendRequestSentForm
        
        return form_class

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user__id=self.request.user.id)
        print(self.get_object().receiver != profile, self.get_object().sender == profile)
        print(self.get_object().receiver, self.get_object().sender, profile)
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if self.get_object().receiver != profile:
            if self.get_object().sender != profile:
            # Redirect the user to somewhere else - add your URL here
                return redirect('profile')

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(FriendRequest, id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Update Friend Request'
        if self.get_object().sender.user == self.request.user:
            context['delete_link'] = True
            context['delete_pk'] = self.kwargs['pk']

        return context

class DeleteFriendRequestView(AccessMixin, DeleteView):
    model = FriendRequest
    template_name = 'home/delete.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if self.get_object().sender.user != self.request.user:
            # Redirect the user to somewhere else - add your URL here
            return redirect('profile')
        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

class FriendRequestListView(ListView):
    model = FriendRequest
    template_name = 'profiles/requests.html'
    context_object_name = 'list_object'
    paginate_by = 12

    def get_queryset(self):
        queryset = FriendRequest.objects.filter(Q(sender__user=self.request.user) | Q (receiver__user=self.request.user))
        return queryset

class RemoveFriendView(AccessMixin, TemplateView, FormMixin):
    template_name = 'home/delete.html'
    success_url = reverse_lazy('profile')
    form_class = FriendRequestForm

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user__id=self.request.user.id)
        view_profile = Profile.objects.get(id=self.kwargs['pk'])
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not profile in view_profile.get_friends():
            # Redirect the user to somewhere else - add your URL here
            return redirect('profile')
        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Profile.objects.get(id=self.kwargs['pk'])
        context['page'] = 'Remove'

        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        profile = Profile.objects.get(user__id=self.request.user.id)
        view_profile = Profile.objects.get(id=self.kwargs['pk'])
        profile.unfriend(view_profile)
            

        return super().form_valid(form)


class SessionRequestListView(ListView):
    model = SessionInvite
    template_name = 'profiles/session_invites.html'
    context_object_name = 'list_object'
    paginate_by = 12

    def get_queryset(self):
        queryset = SessionInvite.objects.filter(Q(receiver__user=self.request.user))
        return queryset

class UserSessionInviteView(AccessMixin, UpdateView):
    model = SessionInvite
    template_name = 'home/form.html'
    success_url = reverse_lazy('profile')

    def get_form_class(self):
        form_class = SessionInviteUpdateForm
        if self.get_object().inbound == True:
            form_class = SessionJoinForm
        
        return form_class

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user__id=self.request.user.id)
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if self.get_object().receiver != profile:
            # Redirect the user to somewhere else - add your URL here
            return redirect('profile')

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(SessionInvite, id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Update Session Invite'
        if self.get_object().inbound == True:
            context['delete_link'] = True
            context['delete_pk'] = self.kwargs['pk']

        return context

class DeleteUserSessionInviteView(AccessMixin, DeleteView):
    model = SessionInvite
    template_name = 'home/delete.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if self.get_object().receiver.user != self.request.user:
            # Redirect the user to somewhere else - add your URL here
            return redirect('profile')
        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)
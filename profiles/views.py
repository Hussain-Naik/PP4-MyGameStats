'''Views for profile app'''
from django.contrib.auth.mixins import AccessMixin
from django.views.generic.edit import UpdateView, FormMixin, DeleteView
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from .models import *


class MyProfileView(LoginRequiredMixin, DetailView):
    '''Profile view for current user'''
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'user_object'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    '''Update profile view'''
    model = Profile
    form_class = CustomUserChangeForm
    template_name = 'home/form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return get_object_or_404(Profile, user__id=self.request.user.id)

    def get_context_data(self, **kwargs):
        '''Add name to form'''
        context = super().get_context_data(**kwargs)
        context['page'] = 'User Update Form'
        return context


class UserProfileView(FormMixin, DetailView):
    '''Profile view for other users'''
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
        FriendRequest.objects.get_or_create(
            sender=sender_,
            receiver=receiver_,
            status='pending'
            )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and FriendRequest.objects.filter(
                sender=Profile.objects.get(user__id=self.request.user.id),
                receiver=Profile.objects.get(id=self.kwargs['pk'])).exists():
            context['sendRequest'] = FriendRequest.objects.get(
                sender=Profile.objects.get(user__id=self.request.user.id),
                receiver=Profile.objects.get(id=self.kwargs['pk'])
                )
        else:
            context['sendRequest'] = False
        return context


class FriendSearchView(ListView):
    '''Profile list view'''
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'list_object'
    paginate_by = 12

    def get_queryset(self):
        q = self.request.GET.get(
            'q'
            ) if self.request.GET.get('q') is not None else ''
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
    '''Update friend request view'''
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
    '''Delete friend request view'''
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
    '''Friend request list view'''
    model = FriendRequest
    template_name = 'profiles/requests.html'
    context_object_name = 'list_object'
    paginate_by = 12

    def get_queryset(self):
        q = self.request.GET.get(
            'q'
            ) if self.request.GET.get('q') is not None else ''
        queryset = FriendRequest.objects.filter(
            Q(sender__user=self.request.user) |
            Q(receiver__user=self.request.user)
            ).filter(
                Q(sender__first_name__icontains=q) |
                Q(sender__last_name__icontains=q) |
                Q(receiver__first_name__icontains=q) |
                Q(receiver__last_name__icontains=q) |
                Q(receiver__user__username__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        return context


class RemoveFriendView(AccessMixin, TemplateView, FormMixin):
    '''Remove Friend view'''
    template_name = 'home/delete.html'
    success_url = reverse_lazy('profile')
    form_class = FriendRequestForm

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(user__id=self.request.user.id)
        view_profile = Profile.objects.get(id=self.kwargs['pk'])
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if profile not in view_profile.get_friends():
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
    '''Session request list view'''
    model = SessionInvite
    template_name = 'profiles/session_invites.html'
    context_object_name = 'list_object'
    paginate_by = 12

    def get_queryset(self):
        q = self.request.GET.get(
            'q'
            ) if self.request.GET.get('q') is not None else ''
        queryset = SessionInvite.objects.filter(
            Q(receiver__user=self.request.user)
            ).filter(
                Q(session__location__icontains=q) |
                Q(session__time__icontains=q) |
                Q(session__admin__username__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        return context


class UserSessionInviteView(AccessMixin, UpdateView):
    '''Update session invite view'''
    model = SessionInvite
    template_name = 'home/form.html'
    success_url = reverse_lazy('profile')

    def get_form_class(self):
        form_class = SessionInviteUpdateForm
        if self.get_object().inbound is True:
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
        if self.get_object().inbound is True:
            context['delete_link'] = True
            context['delete_pk'] = self.kwargs['pk']

        return context


class DeleteUserSessionInviteView(AccessMixin, DeleteView):
    '''Delete session invite view'''
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

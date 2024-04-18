from .models import *
from django.views.generic.edit import CreateView, UpdateView, FormMixin, DeleteView
from django.contrib.auth.mixins import AccessMixin
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class GroupListView(ListView):
    model = Group
    template_name = 'events/group_list.html'
    context_object_name = 'list_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['list_object'] = Group.objects.filter(Q(sessions__session_roster__player=self.request.user) | Q(host=self.request.user.id) | Q(private=False)).distinct()
        else:
            context['list_object'] = Group.objects.filter(private=False)
        return context

class CreateGroupView(LoginRequiredMixin, CreateView):
    form_class = GroupCreationForm
    template_name = 'home/form.html'
    success_url = reverse_lazy('groups')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Group Creation Form'
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.host = self.request.user
        obj.save()
        return super().form_valid(form)

class GroupDetailView(AccessMixin, DetailView):
    model = Group
    template_name = 'events/group_detail.html'
    context_object_name = 'detail_object'

    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not User.objects.filter(session__group=group.id, id=self.request.user.id).exists() | group.host.id == self.request.user.id:
            # Redirect the user to somewhere else - add your URL here
            if group.private:
                return redirect('groups')

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)
'''Views for Events app'''
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormMixin, DeleteView
from django.contrib.auth.mixins import AccessMixin
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *


class GroupListView(ListView):
    '''Group list view'''
    model = Group
    template_name = 'events/group_list.html'
    context_object_name = 'list_object'
    paginate_by = 12

    def get_queryset(self):
        '''filter queryset to display open and only participating groups'''
        q = self.request.GET.get(
            'q'
            ) if self.request.GET.get('q') is not None else ''
        if self.request.user.is_authenticated:
            queryset = Group.objects.filter(
                Q(sessions__session_roster__player=self.request.user) |
                Q(host=self.request.user.id) |
                Q(private=False)
                ).distinct().filter(
                    Q(name__icontains=q)
                )
        else:
            queryset = Group.objects.filter(
                Q(private=False) |
                Q(name__icontains=q)
                )
        return queryset

    def get_context_data(self, **kwargs):
        '''Add extra context for list search feature'''
        context = super().get_context_data(**kwargs)
        context['search'] = True
        return context


class CreateGroupView(LoginRequiredMixin, CreateView):
    '''View to create new group'''
    form_class = GroupCreationForm
    template_name = 'home/form.html'
    success_url = reverse_lazy('groups')

    def get_context_data(self, **kwargs):
        '''Add extra context for form name as page'''
        context = super().get_context_data(**kwargs)
        context['page'] = 'Group Creation Form'
        return context

    def form_valid(self, form):
        '''Form submit to auto assign host as logged user'''
        obj = form.save(commit=False)
        obj.host = self.request.user
        obj.save()
        return super().form_valid(form)


class GroupDetailView(AccessMixin, DetailView):
    '''Group detail view'''
    model = Group
    template_name = 'events/group_detail.html'
    context_object_name = 'detail_object'

    def dispatch(self, request, *args, **kwargs):
        '''Check user access'''
        group = self.get_object()
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if self.request.user not in group.get_all_participants():
            # Redirect the user to somewhere else - add your URL here
            if self.request.user != group.host:
                return redirect('groups')

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)


class UpdateGroupView(LoginRequiredMixin, UpdateView):
    '''Update group view'''
    form_class = GroupCreationForm
    template_name = 'home/form.html'
    context_object_name = 'detail_object'

    def get_success_url(self):
        return reverse_lazy(
            'group_detail',
            kwargs={"pk": self.get_object().id}
            )

    def get_context_data(self, **kwargs):
        '''Display form name as page value'''
        context = super().get_context_data(**kwargs)
        context['page'] = 'Group Update Form'
        return context

    def get_object(self):
        return get_object_or_404(Group, id=self.kwargs['pk'])


class CreateSessionView(LoginRequiredMixin, CreateView):
    '''Create session view'''
    form_class = SessionCreationForm
    template_name = 'home/form.html'
    success_url = reverse_lazy('groups')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Session Creation Form'
        context['detail_object'] = Group.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.admin = self.request.user
        obj.group = Group.objects.get(id=self.kwargs['pk'])
        obj.save()
        obj.players.add(self.request.user, through_defaults={'roster': 1})
        return super().form_valid(form)


class UpdateSessionView(AccessMixin, UpdateView):
    '''Update session view'''
    form_class = SessionUpdateForm
    template_name = 'home/form.html'
    context_object_name = 'detail_object'

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if User.objects.filter(
                session__group=self.get_object().group.id,
                id=self.request.user.id
                ).exists() is not True:
            if self.get_object().admin.id != self.request.user.id:
                # Redirect the user to somewhere else - add your URL here
                return redirect('group_detail', pk=self.get_object().group.id)
            else:
                pass

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('session',  kwargs={"pk": self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Session Update Form'
        return context

    def get_object(self):
        return get_object_or_404(Session, id=self.kwargs['pk'])


class UpdateSessionAdminView(AccessMixin, UpdateView):
    '''Update session admin view'''
    form_class = SessionUpdateAdminForm
    template_name = 'home/form.html'
    context_object_name = 'detail_object'

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display members that belong to a given user
        """

        kwargs = super(UpdateSessionAdminView, self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if User.objects.filter(
                session__group=self.get_object().group.id,
                id=self.request.user.id
                ).exists() is not True:
            if self.get_object().admin.id != self.request.user.id:
                # Redirect the user to somewhere else - add your URL here
                return redirect('group_detail', pk=self.get_object().group.id)
            else:
                pass

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('session',  kwargs={"pk": self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Change Session Admin'
        return context

    def get_object(self):
        return get_object_or_404(Session, id=self.kwargs['pk'])


class UpdateGroupAdminView(AccessMixin, UpdateView):
    '''Update group host view'''
    form_class = GroupUpdateAdminForm
    template_name = 'home/form.html'
    context_object_name = 'detail_object'

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display members that belong to a given user
        """

        kwargs = super(UpdateGroupAdminView, self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if self.get_object().host.id != self.request.user.id:
            return redirect('group_detail', pk=self.get_object().id)

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(
            'group_detail',
            kwargs={"pk": self.get_object().id}
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Change Group Host'
        return context

    def get_object(self):
        return get_object_or_404(Group, id=self.kwargs['pk'])


class SessionDetailView(AccessMixin, FormMixin, DetailView):
    '''Session detail view'''
    template_name = 'events/session_detail.html'
    model = Session
    context_object_name = 'detail_object'
    form_class = GameCreationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invited_profiles = Profile.objects.filter(
            session_invite_receiver__session=self.get_object()
            )
        invited_users = User.objects.filter(profile__id__in=invited_profiles)
        context['session_invites'] = invited_users
        return context

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if User.objects.filter(
                session__group=self.get_object().group.id,
                id=self.request.user.id
                ).exists() is not True:
            if self.get_object().admin.id != self.request.user.id:
                # Redirect the user to somewhere else - add your URL here
                return redirect('group_detail', pk=self.get_object().group.id)
            else:
                pass

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display members that belong to a given user
        """

        kwargs = super(SessionDetailView, self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self):
        game = Session.objects.get(id=self.kwargs['pk']).session_games.last()
        return reverse_lazy("game", kwargs={"pk": game.pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if form.data['choice'] == '':
            Game.objects.create(session=self.get_object())
        else:
            roster = self.get_object().session_roster.all().order_by('roster')
            matchup = Matchup.objects.get(id=form.data['choice'])
            team1 = Team.objects.filter(
                team_players=roster[matchup.team1_player1_index - 1].player
                ).filter(
                    team_players=roster[matchup.team1_player2_index - 1].player
                    )
            team2 = Team.objects.filter(
                team_players=roster[matchup.team2_player1_index - 1].player
                ).filter(
                    team_players=roster[matchup.team2_player2_index - 1].player
                    )

            if not team1.exists():
                new_team = Team.objects.create()
                new_team.team_players.set(
                    [roster[matchup.team1_player1_index - 1].player,
                     roster[matchup.team1_player2_index - 1].player]
                    )
                team1 = new_team
            else:
                team1 = team1.first()

            if not team2.exists():
                new_team2 = Team.objects.create()
                new_team2.team_players.set(
                    [roster[matchup.team2_player1_index - 1].player,
                     roster[matchup.team2_player2_index - 1].player]
                     )
                team2 = new_team2
            else:
                team2 = team2.first()

            manual_game = Game.objects.create(
                session=self.get_object(),
                creation_type='manual'
                )
            manual_game.team.set([team1, team2])

        return super().form_valid(form)


class GameDetailView(AccessMixin, FormMixin, DetailView):
    '''Game detail view'''
    template_name = 'events/game_detail.html'
    model = Game
    context_object_name = 'detail_object'
    form_class = TeamScoreForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not Game.objects.filter(
                id=self.get_object().id
                ).filter(session__admin=self.request.user).exists():
            # Redirect the user to somewhere else - add your URL here
            return redirect('session', pk=self.get_object().session.id)

            # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        game = Game.objects.get(id=self.kwargs['pk'])
        return reverse_lazy("session", kwargs={"pk": game.session.id})

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display members that belong to a given user
        """

        kwargs = super(GameDetailView, self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        game = Game.objects.get(id=self.kwargs['pk'])
        team1 = Fixture.objects.get(game=game, team=game.team1)
        team1.score = form.data['team1_score']

        team2 = Fixture.objects.get(game=game, team=game.team2)
        team2.score = form.data['team2_score']
        if team1.score > team2.score:
            team1.is_winner = True
            team2.is_winner = False
        elif team2.score > team1.score:
            team1.is_winner = False
            team2.is_winner = True
        else:
            pass

        team1.save()
        team2.save()
        game.session.set_winner()
        return super().form_valid(form)


class SessionInviteView(LoginRequiredMixin, ListView):
    '''Session invite view'''
    model = SessionInvite
    template_name = 'events/session_invites.html'
    context_object_name = 'list_object'
    paginate_by = 12

    def get_queryset(self):
        queryset = SessionInvite.objects.filter(
            session=self.kwargs['pk'],
            status='pending'
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session_pk'] = self.kwargs['pk']
        context['roster'] = Roster.objects.filter(session=self.kwargs['pk'])
        context['detail_object'] = Session.objects.get(id=self.kwargs['pk'])
        context['page'] = 'Session Invites'
        return context


class CreateSessionInviteView(LoginRequiredMixin, CreateView):
    '''Session invite create view'''
    model = SessionInvite
    form_class = SessionInviteForm
    template_name = 'home/form.html'

    def get_success_url(self):
        return reverse_lazy('session_invite', kwargs={"pk": self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Send Session Invite'
        context['detail_object'] = Session.objects.get(id=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display members that belong to a given user
        """

        kwargs = super(CreateSessionInviteView, self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        kwargs['user'] = self.request.user.id
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.session = Session.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class RosterPlayerRemoveView(AccessMixin, DeleteView):
    '''Remove player from session view'''
    model = Roster
    template_name = 'home/delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'session_invite',
            kwargs={"pk": self.get_object().session.id}
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_object'] = Session.objects.get(
                id=self.get_object().session.id
                )
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not User.objects.filter(
                session__admin=self.request.user,
                session__id=self.get_object().session.id
                ).exists():
            # Redirect the user to somewhere else - add your URL here
            return redirect('session', pk=self.get_object().session.id)
        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)


class DeleteSessionInvite(AccessMixin, DeleteView):
    '''Delete session invite view'''
    model = SessionInvite
    template_name = 'home/delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'session_invite',
            kwargs={"pk": self.get_object().session.id}
            )

    def get_context_data(self, **kwargs):
        session_invite = SessionInvite.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['detail_object'] = session_invite.session
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not User.objects.filter(
                session__admin=self.request.user,
                session__id=self.get_object().session.id
                ).exists():
            # Redirect the user to somewhere else - add your URL here
            return redirect('session', pk=self.get_object().session.id)
        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)


class DeleteSession(AccessMixin, DeleteView):
    '''Delete session view'''
    model = Session
    template_name = 'home/delete.html'
    context_object_name = 'detail_object'

    def get_success_url(self):
        return reverse_lazy(
            'group_detail',
            kwargs={"pk": self.get_object().group.id}
            )

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not User.objects.filter(
                session__admin=self.request.user,
                session__id=self.get_object().id
                ).exists():
            # Redirect the user to somewhere else - add your URL here
            return redirect('session', pk=self.get_object().session.id)
        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)


class DeleteGroup(AccessMixin, DeleteView):
    '''Delete group view'''
    model = Group
    template_name = 'home/delete.html'
    context_object_name = 'detail_object'

    def get_success_url(self):
        return reverse_lazy('groups')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not User.objects.filter(
                group_author__host=self.request.user,
                group_author__id=self.get_object().id
                ).exists():
            # Redirect the user to somewhere else - add your URL here
            return redirect('groups')
        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)


class UpdateSessionInviteView(AccessMixin, UpdateView):
    '''Update session invite view'''
    form_class = SessionInviteUpdateForm
    template_name = 'home/form.html'
    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get(
            'HTTP_REFERER', self.default_redirect
            )
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if self.get_object().inbound is True:
            if self.get_object().session.admin.id != self.request.user.id:
                return redirect(
                    'session_invite',
                    pk=self.get_object().session.id
                    )
        else:
            if self.get_object().receiver.user.id != self.request.user.id:
                return redirect(
                    'session_invite',
                    pk=self.get_object().session.id
                    )

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Update Session Invite Form'
        context['detail_object'] = Session.objects.get(
                                    id=self.get_object().session.id
                                    )
        return context

    def get_object(self):
        return get_object_or_404(SessionInvite, id=self.kwargs['pk'])


class CreateSessionJoinView(LoginRequiredMixin, CreateView):
    '''View to create session join request'''
    model = SessionInvite
    form_class = SessionJoinForm
    template_name = 'events/session_join.html'

    def get_success_url(self):
        return reverse_lazy('session',  kwargs={"pk": self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Session Join Request'
        context['detail_object'] = Session.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.session = Session.objects.get(id=self.kwargs['pk'])
        obj.receiver = Profile.objects.get(user__id=self.request.user.id)
        obj.inbound = True
        return super().form_valid(form)

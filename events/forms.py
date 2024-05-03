'''Forms for the Events app'''
from django import forms
from django.db.models import Q
from django.forms import Form, ModelForm, HiddenInput
from .models import Game, Group, Session, Matchup
from django.contrib.auth.models import User
from profiles.models import SessionInvite, Profile


class GroupCreationForm(ModelForm):
    '''From to create new group'''
    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'private':
                field_id = 'floating' + field
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control',
                     'placeholder': field.capitalize(),
                     'id': field_id}
                    )
            else:
                field_id = field
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input float-end',
                     'role': 'switch', 'id': field_id,
                     'data-bs-toggle': 'collapse',
                     'data-bs-target': '#privateInfo'}
                    )

    class Meta:
        '''Meta class'''
        model = Group
        exclude = ['host']


class SessionCreationForm(ModelForm):
    '''From to create new sessions'''
    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(SessionCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            field_id = 'floating' + field
            if field == 'game_type' or field == 'team_selection':
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control',
                     'id': field_id}
                    )
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control',
                     'placeholder': field.capitalize(),
                     'id': field_id}
                    )

    class Meta:
        '''Meta class'''
        model = Session
        exclude = ['status', 'joinable', 'admin', 'players', 'group']


class SessionUpdateForm(ModelForm):
    '''From to update session'''
    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(SessionUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            field_id = 'floating' + field
            if field == 'game_type' or field == 'team_selection':
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control',
                     'id': field_id}
                    )
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control',
                     'placeholder': field.capitalize(),
                     'id': field_id}
                    )

    class Meta:
        '''Meta class'''
        model = Session
        exclude = ['status', 'joinable', 'players', 'group', 'admin']


class SessionUpdateAdminForm(ModelForm):
    '''From to update session admin'''
    def __init__(self, *args, **kwargs):
        '''
        Add bootstrap floating input field styling
        And populate option to only participating users
        '''
        session = Session.objects.get(id=kwargs.pop('pk'))
        super(SessionUpdateAdminForm, self).__init__(*args, **kwargs)
        self.fields['admin'].queryset = User.objects.filter(
            id__in=session.players.all()
        )
        for field in self.fields:
            field_id = 'floating' + field
            self.fields[field].widget.attrs.update(
                {'class': 'form-control',
                 'id': field_id}
                )

    class Meta:
        '''Meta class'''
        model = Session
        fields = ['admin']


class GroupUpdateAdminForm(ModelForm):
    '''From to update group host'''
    def __init__(self, *args, **kwargs):
        '''
        Add bootstrap floating input field styling
        And populate option to only participating users
        '''
        group = Group.objects.get(id=kwargs.pop('pk'))
        super(GroupUpdateAdminForm, self).__init__(*args, **kwargs)
        self.fields['host'].queryset = User.objects.filter(
            id__in=group.get_all_participants()
            )
        for field in self.fields:
            field_id = 'floating' + field
            self.fields[field].widget.attrs.update(
                {'class': 'form-control',
                 'id': field_id}
                )

    class Meta:
        '''Meta class'''
        model = Group
        fields = ['host']


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, game):
        return "%s" % game.name


class GameCreationForm(Form):
    '''From to create new game'''
    def __init__(self, *args, **kwargs):
        '''
        Add bootstrap floating input field styling
        Grants access to the request object so that only members
        of the current user are given as options
        '''

        session = Session.objects.get(id=kwargs.pop('pk'))
        super(GameCreationForm, self).__init__(*args, **kwargs)
        # self.fields['choice'].queryset = ['Next Match']
        self.fields['choice'].queryset = Matchup.objects.filter(
            player_count=session.player_count)
        self.fields['choice'].required = False
        self.fields['choice'].widget.attrs.update(
            {'class': 'form-select',
             'id': 'floatingChoice'}
            )

    choice = CustomModelChoiceField(
        queryset=None,
    )


class TeamScoreForm(Form):
    '''From to input team scores'''

    team1_score = forms.IntegerField()
    team2_score = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        game = Game.objects.get(id=kwargs.pop('pk'))
        super(TeamScoreForm, self).__init__(*args, **kwargs)
        self.fields["team1_score"].initial = game.game_fixture.get(
            team=game.team1
            ).score
        self.fields["team2_score"].initial = game.game_fixture.get(
            team=game.team2
            ).score
        self.fields["team1_score"].widget.attrs.update(
            {'class': 'form-control',
             'id': 'team1_score'}
            )
        self.fields["team2_score"].widget.attrs.update(
            {'class': 'form-control',
             'id': 'team2_score'}
            )


class SessionInviteForm(ModelForm):
    '''From to create session invites'''
    def __init__(self, *args, **kwargs):
        '''
        Add bootstrap floating input field styling
        and filter option queryset based on users participating in group,
        user friend list and exclude users awaiting current session invite or
        already joined
        '''
        session = Session.objects.get(id=kwargs.pop('pk'))
        user = Profile.objects.get(user_id=kwargs.pop('user'))
        session_invited = Profile.objects.filter(
            session_invite_receiver__session=session.id
            )
        super(SessionInviteForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].queryset = Profile.objects.filter(
            Q(user__id__in=session.group.get_all_participants()) |
            Q(id__in=user.friends.all())
            ).exclude(
                Q(user__id__in=session.players.all()) |
                Q(id__in=session_invited)
                )
        for field in self.fields:
            field_id = 'floating' + field
            self.fields[field].widget.attrs.update(
                {'class': 'form-control',
                 'id': field_id}
                )

    class Meta:
        '''Meta class'''
        model = SessionInvite
        fields = ['receiver']


class SessionInviteUpdateForm(ModelForm):
    '''From to update session invites'''
    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(SessionInviteUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            field_id = field
            self.fields[field].widget.attrs.update(
                {'class': 'form-control',
                 'id': field_id}
                )

    class Meta:
        '''Meta class'''
        model = SessionInvite
        fields = ['status']


class SessionJoinForm(ModelForm):
    '''From to create session join request'''

    class Meta:
        '''Meta class'''
        model = SessionInvite
        fields = ['inbound']
        widgets = {'inbound': HiddenInput(), }

from django import forms
from django.forms import Form, ModelForm
from .models import Game, Group ,Session, Fixture, Matchup

class GroupCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'private':
                form_id = 'floating' + field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': form_id})
            else:
                form_id = field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-check-input float-end', 'role': 'switch','id': form_id})

    class Meta:
        model = Group
        exclude = ['host']

class SessionCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SessionCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': 'floatingEmail'})

    class Meta:
        model = Session
        exclude = ['status', 'joinable', 'admin', 'players', 'group']

class SessionUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SessionUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': 'floatingEmail'})

    class Meta:
        model = Session
        exclude = ['status', 'joinable', 'players', 'group']

class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, game):
        return "%s" % game.name

class GameCreationForm(Form):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        session = Session.objects.get(id=kwargs.pop('pk'))
        super(GameCreationForm, self).__init__(*args, **kwargs)
        # self.fields['choice'].queryset = ['Next Match']
        self.fields['choice'].queryset = Matchup.objects.filter(
            player_count=session.player_count)
        self.fields['choice'].required = False
        self.fields['choice'].widget.attrs.update({'class': 'form-select', 'placeholder': '', 'id': 'floatingChoice'})
    
    choice = CustomModelChoiceField(
        queryset=None,
    )

class TeamScoreForm(Form):
    def __init__(self, *args, **kwargs):
        game = Game.objects.get(id=kwargs.pop('pk'))
        super(TeamScoreForm, self).__init__(*args, **kwargs)
        self.fields["team1_score"].initial = game.game_fixture.get(team=game.team1).score
        self.fields["team2_score"].initial = game.game_fixture.get(team=game.team2).score
        self.fields["team1_score"].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': 'floatingScore1'})
        self.fields["team2_score"].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': 'floatingScore2'})


    team1_score = forms.IntegerField()
    team2_score = forms.IntegerField()
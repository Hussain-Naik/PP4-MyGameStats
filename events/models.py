'''Models for the events app'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q, Count, Max


class Group(models.Model):
    """Group event model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    host = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='group_author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        """group model string representation"""
        return self.name

    def get_group_id(self):
        '''method to return group id'''
        return self.id

    def get_all_participants(self):
        '''method to return queryset of all participating users in group'''
        queryset = User.objects.filter(session__group=self).distinct()
        queryset = queryset.annotate(
            session_wins=Count(
                'roster', filter=Q(session__session_roster__is_winner=True)
                )
            )
        return queryset


class Session(models.Model):
    """Event session model"""
    STATUS = (
        (1, 'open'),
        (2, 'in progress'),
        (3, 'completed'),
    )
    GAME_TYPE = [(1, 'Doubles'), ]
    TEAM_TYPE = [(1, 'Random'), ]

    location = models.CharField(max_length=30, blank=False)
    time = models.CharField(max_length=30, blank=False)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='sessions')
    players = models.ManyToManyField(
        User, through='Roster', related_name='session'
        )
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='session_admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    joinable = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=1)
    game_type = models.IntegerField(choices=GAME_TYPE, default=1)
    team_selection = models.IntegerField(choices=TEAM_TYPE, default=1)

    def __str__(self):
        """Sessions model string representation"""
        return self.name

    @property
    def player_count(self):
        '''session property to display number of players'''
        return self.players.count()

    @property
    def name(self):
        '''session property to display name'''
        return self.location + ' ' + self.time

    def get_group_id(self):
        '''method to return session group id'''
        return self.group.id

    def get_min_player_needed(self):
        '''
        method to return minimum number of players required to start games
        '''
        return self.status * 4

    def add_next_game(self):
        '''method to create next session game'''
        Game.objects.create(session=self)

    def get_session_games(self):
        '''method to get count of all games in current session'''
        return self.session_games.count()

    def get_session_roster(self):
        '''method to return queryset of roster'''
        return self.session_roster.all().order_by('roster')

    def add_player(self, user):
        '''method to add player to session'''
        return self.players.add(
            user, through_defaults={'roster': self.player_count + 1}
            )

    def set_winner(self):
        '''method to update session winner based on the number of games won'''
        query = User.objects.filter(
            roster__session=self.id
            ).annotate(
                games_won=Count(
                    'team',
                    filter=Q(team__team_fixture__is_winner=True) &
                    Q(team__team_fixture__game__session=self.id)
                    )
                )
        max_score = query.aggregate(highest_score=Max('games_won'))
        losers = query.filter(games_won__lt=max_score['highest_score'])
        winner = query.filter(games_won__exact=max_score['highest_score'])

        roster_query = Roster.objects.filter(
            session=self.id, player__in=winner
            )
        roster_query.update(is_winner=True)
        roster_query = Roster.objects.filter(
            session=self.id, player__in=losers
            )
        roster_query.update(is_winner=False)

        return winner

    def get_winner(self):
        '''method to return winner as user object'''
        return User.objects.filter(
            roster__session=self.id,
            roster__is_winner=True
            )


class Roster(models.Model):
    """Associated model for session and users"""
    player = models.ForeignKey(
        User, on_delete=models.DO_NOTHING,
        related_name='roster'
        )
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE,
        related_name='session_roster'
        )
    roster = models.IntegerField()
    is_winner = models.BooleanField(default=False)

    def get_session_games_won(self):
        '''method to return value of games won by the current player'''
        return User.objects.filter(
            roster__player=self.player,
            roster__session=self.session
            ).annotate(games_won=Count(
                'team',
                filter=Q(team__team_fixture__is_winner=True) &
                Q(team__team_fixture__game__session=self.session)
                )
            )

    def get_session_wins(self):
        '''method to return number of session wins by the current player'''
        return User.objects.filter(
            roster__player=self.player,
            roster__session__group=self.session.group
            ).distinct()


class Team(models.Model):
    '''Badminton team model'''
    team_players = models.ManyToManyField(User, related_name='team')

    def __str__(self):
        """Team model string representation"""
        return self.name

    @property
    def name(self):
        '''model property for team name'''
        return 'Team ' + str(self.pk)

    @property
    def players(self):
        '''model property to display users in team'''
        team = ", ".join(
            str(player.username) for player in self.team_players.all()
            )
        return team

    def get_all_games_played(self):
        '''method to return number of games played by team'''
        return Game.objects.filter(team=self).count()

    def get_all_games_won(self):
        '''Method to return number of games won by team'''
        return Fixture.objects.filter(team=self, is_winner=True).count()

    def get_all_games_lost(self):
        '''Method to return number of games lost by team'''
        return Fixture.objects.filter(team=self, is_winner=False).count()

    def pairing(self, current):
        '''Method to return name participating team member'''
        return ", ".join(
            str(player.username) for player in self.team_players.all().exclude(
                id=current.user.id)
                )


class Fixture(models.Model):
    '''Badminton fixture model to keep track of game outcomes'''
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE,
        related_name='team_fixture'
        )
    game = models.ForeignKey(
        'Game', on_delete=models.CASCADE,
        related_name='game_fixture'
        )
    score = models.IntegerField(default=0)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        '''String representation of Fixture model'''
        return "{}:{}".format(self.game, self.players)

    @property
    def players(self):
        '''model property to display name of team players'''
        return self.team.players


class Game(models.Model):
    """Game model"""
    STATUS_CHOICES = (
        ('manual', 'manual'),
        ('sequence', 'sequence'),
    )

    inc = models.IntegerField(default=0)
    creation_type = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default='sequence'
        )
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE,
        related_name='session_games',
        null=True
        )
    team = models.ManyToManyField(Team, through=Fixture)

    @property
    def name(self):
        '''model property to display the game name'''
        return 'Game ' + str(self.inc)

    @property
    def winning_team(self):
        '''model property to display winning team'''
        t_g_1 = Fixture.objects.get(game=self, team=self.team1)
        t_g_2 = Fixture.objects.get(game=self, team=self.team2)
        if (t_g_1.score > t_g_2.score):
            return self.team1
        elif (t_g_2.score > t_g_1.score):
            return self.team2
        else:
            return (self.team1, self.team2)

    @property
    def team1(self):
        '''model property to display game team 1'''
        return self.team.all().order_by('id').first()

    @property
    def team2(self):
        '''model property to display game team 2'''
        return self.team.all().order_by('-id').first()

    def __str__(self):
        """Game model string representation"""
        return self.name

    def save(self, *args, **kwargs):
        '''method to save model increment value'''
        if Game.objects.filter(id=self.id).exists():
            offset = self.inc - 1
        else:
            offset = Game.objects.filter(session=self.session).count()
        self.inc = offset + 1
        super().save(*args, **kwargs)

    def get_group_id(self):
        return self.session.group.id


class Matchup(models.Model):
    '''Matchup model'''

    player_count = models.IntegerField()
    game_index = models.IntegerField()
    team1_player1_index = models.IntegerField()
    team1_player2_index = models.IntegerField()
    team2_player1_index = models.IntegerField()
    team2_player2_index = models.IntegerField()

    def __str__(self):
        '''String representation of Matchup model'''
        pc = self.player_count
        gi = self.game_index
        return f'Players: {str(pc)} Game: {str(gi)} Match: {self.name}'

    @property
    def name(self):
        '''model property to display team variations'''
        w = self.team1_player1_index
        x = self.team1_player2_index
        y = self.team2_player1_index
        z = self.team2_player2_index
        return f'Player {w} & Player {x} vs Player {y} & Player {z}'

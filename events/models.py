from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    """Group event model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    slug = models.SlugField(unique=True, blank=False)
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='group_admin')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    private_group = models.BooleanField(default=False)

    def __str__(self):
        """Events model string representation"""
        return self.name

class Sessions(models.Model):
    STATUS = (
    (1, 'open'),
    (2, 'in progress'),
    (3, 'completed'),
    )
    GAME_TYPE = ((1, 'Singles'),(2, 'Doubles'))
    TEAM_TYPE = ((1, 'Random'),(2, 'User Defined'))
    """Event session model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='sessions')
    players = models.ManyToManyField(User, through='PlayerSessions', related_name='session')
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
        return self.name + ' ' + self.created_at
    
    @property
    def player_count(self):
        return self.players.count()
    
class PlayerSessions(models.Model):
    """Associated model for group and users"""
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)


class Game(models.Model):
    """Game model"""
    inc = models.IntegerField(default=0)
    session = models.ForeignKey(
        Sessions, on_delete=models.CASCADE, related_name='session_games')
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='game_admin')
    team_1_score = models.IntegerField(default=0)
    team_1_player1 = models.IntegerField(blank=False, null=False)
    team_1_player2 = models.IntegerField(blank=True, null=True)
    team_2_score = models.IntegerField(default=0)
    team_2_player1 = models.IntegerField(blank=False, null=False)
    team_2_player2 = models.IntegerField(blank=True, null=True)

    @property
    def name(self):
        return 'Game '+ self.inc
    
    def __str__(self):
        """Game model string representation"""
        return self.name


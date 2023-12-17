from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    """Group event model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    slug = models.SlugField(unique=True, blank=False)
    members = models.ManyToManyField(User, related_name='group', through='Players')
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='group_admin')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Events model string representation"""
        return self.name


class Players(models.Model):
    """Associated model for group and users"""
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    playing = models.BooleanField(default=False)
    wins = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)

class Sessions(models.Model):
    STATUS = (
    (1, 'open'),
    (2, 'in progress'),
    (3, 'completed'),
    )
    """Event session model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='session')
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='session_admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    joinable = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        """Sessions model string representation"""
        return self.name + ' ' + self.created_at
    
    @property
    def player_count(self):
        return self.group.members.count()
    
class SessionScore(models.Model):
    """Session score model"""
    player_id = models.IntegerField(default=0, null=False, blank=False)
    inc = models.IntegerField(default=0)
    player_score = models.IntegerField(default=0)
    session = models.ForeignKey(
        Sessions, on_delete=models.CASCADE, related_name='session_scores')
    
    @property
    def name(self):
        return 'Player '+ self.inc

    def __str__(self):
        """Session score model string representation"""
        return self.name


class Game(models.Model):
    """Game model"""
    inc = models.IntegerField(default=0)
    session = models.ForeignKey(
        Sessions, on_delete=models.CASCADE, related_name='session_games')
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='game_admin')
    team_1_score = models.IntegerField(default=0)
    team_2_score = models.IntegerField(default=0)

    @property
    def name(self):
        return 'Game '+ self.inc
    
    @property
    def team1_player1(self):
        return 1
    
    @property
    def team1_player2(self):
        return 2
    
    @property
    def team2_player1(self):
        return 3
    
    @property
    def team2_player2(self):
        return 4

    def __str__(self):
        """Game model string representation"""
        return self.name


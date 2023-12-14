from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    """Group event model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    slug = models.SlugField(unique=True, blank=False)
    members = models.ManyToManyField(User, related_name='events')
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='event_admin')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Events model string representation"""
        return self.name

class Sessions(models.Model):
    STATUS = (
    (1, 'open'),
    (2, 'in progress'),
    (3, 'completed'),
    )
    """Event session model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='session')
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='session_admin')
    players = models.ManyToManyField(User, related_name='session_players')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    joinable = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        """Sessions model string representation"""
        return self.name + ' ' + self.created_at

class Game(models.Model):
    STATUS = (
    (1, 'open'),
    (2, 'in progress'),
    (3, 'completed'),
    )
    """Game model"""
    name = models.CharField(max_length=30, unique=True, blank=False)
    session = models.ForeignKey(
        Sessions, on_delete=models.CASCADE, related_name='session_games')
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='game_admin')
    team_1 = models.IntegerField(default=0)
    team_2 = models.IntegerField(default=0)
    team_1_score = models.IntegerField(default=0)
    team_2_score = models.IntegerField(default=0)

    def __str__(self):
        """Game model string representation"""
        return self.name

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from events.models import *

# Create your models here.
class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    first_name = models.CharField(max_length=25,blank=True,null=True)
    last_name = models.CharField(max_length=25,blank=True,null=True)
    friends = models.ManyToManyField('Profile' ,blank=True)

    def __str__(self):
        """Profile model string representation"""
        return self.user.username
    
    def get_friends(self):
        return self.friends.all()
    
    def get_friends_count(self):
        return self.friends.all().count()

    def add_friend(self, profile):
        if not profile in self.friends.all():
            self.friends.add(profile)
    
    def remove_friend(self, profile):
        if profile in self.friends.all():
            self.friends.remove(profile)

    def unfriend(self, removee):
        self.remove_friend(removee)
        self.save()

        removee_profile = Profile.objects.get(id=removee.id)
        removee_profile.remove_friend(self)
        removee_profile.save()
    
    def get_pending_requests(self):
        return FriendRequest.objects.filter(Q(sender=self.id) | Q(receiver=self.id))[:5]
    
    def all_pending_requests(self):
        return FriendRequest.objects.filter(Q(sender=self.id) | Q(receiver=self.id))
    
    def get_session_invites(self):
        return SessionInvite.objects.filter(Q(receiver=self.id))[:5]
    
    def all_session_invites(self):
        return SessionInvite.objects.filter(Q(receiver=self.id))
    
    def get_all_games_played(self):
        return Game.objects.filter(game_fixture__team__team_players=self.user.id).count()
    
    def get_all_games_won(self):
        return Game.objects.filter(game_fixture__team__team_players=self.user.id, game_fixture__is_winner=True).count()
    
    def get_all_games_lost(self):
        return Game.objects.filter(game_fixture__team__team_players=self.user.id, game_fixture__is_winner=False).count()
    
    def get_all_session_wins(self):
        return Roster.objects.filter(player=self.user.id, is_winner=True).count()
    
    def get_session_wins(self, group):
        print(Roster.objects.filter(player=self.user.id, session__group=group.id, is_winner=True))
        return Roster.objects.filter(player=self.user.id, session__group=group.id, is_winner=True).count()
    
    def get_group_game_wins(self, group):
        return Game.objects.filter(game_fixture__team__team_players=self.user.id, session__group=group, game_fixture__is_winner=True).count()
    

class FriendRequest(models.Model):
    """Friend Request model"""
    STATUS_CHOICES = (
        ('send', 'send'),
        ('accepted', 'accepted'),
    )
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='friend_request_from_profile'
    )
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='friend_request_to_profile'
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    sent_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Friend Request model string representation"""
        return f'{self.sender} to {self.receiver}'
    

class SessionInvite(models.Model):
    """Session Invite model"""
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('declined', 'declined'),
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='session_invite'
    )
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='session_invite_receiver'
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
    inbound = models.BooleanField(default=False)
    sent_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Friend Request model string representation"""
        if self.inbound == True:
            return f'{self.receiver} requested to join {self.session}'
        return f'{self.receiver} invited to {self.session}'
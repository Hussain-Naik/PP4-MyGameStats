'''models for profile app'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from events.models import *


class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    friends = models.ManyToManyField('Profile', blank=True)

    def __str__(self):
        """Profile model string representation"""
        return self.user.username

    def profile_avatar(self):
        '''method to return user initials or username with preceding u '''
        if self.first_name is None or self.last_name is None:
            return 'u' + self.user.username[0]
        return self.first_name[0] + self.last_name[0]

    def get_friends(self):
        '''method to return first seven friends for profile'''
        return self.friends.all()[:7]

    def remaining_friends_count(self):
        '''method to return remaing friends counter'''
        return self.get_friends_count() - 7

    def get_friends_all(self):
        '''method to return all friends'''
        return self.friends.all()

    def get_friends_count(self):
        '''method to return number of friends'''
        return self.friends.all().count()

    def add_friend(self, profile):
        '''model method to add friends'''
        if profile not in self.friends.all():
            self.friends.add(profile)

    def remove_friend(self, profile):
        '''model method to remove friends'''
        if profile in self.friends.all():
            self.friends.remove(profile)

    def unfriend(self, removee):
        '''model method that unfriends two users'''
        self.remove_friend(removee)
        self.save()

        removee_profile = Profile.objects.get(id=removee.id)
        removee_profile.remove_friend(self)
        removee_profile.save()

    def get_pending_requests(self):
        '''model method to return first 5 friends requests for profile view'''
        return FriendRequest.objects.filter(
            Q(sender=self.id) |
            Q(receiver=self.id)
            )[:5]

    def all_pending_requests(self):
        '''model method to return all pending friend requests'''
        return FriendRequest.objects.filter(
            Q(sender=self.id) |
            Q(receiver=self.id)
            )

    def get_session_invites(self):
        '''Method to return first 5 session invites'''
        return SessionInvite.objects.filter(Q(receiver=self.id))[:5]

    def all_session_invites(self):
        '''Method to return all session invites'''
        return SessionInvite.objects.filter(Q(receiver=self.id))

    def get_all_games_played(self):
        '''Method to return number of games played by user'''
        return Game.objects.filter(
            game_fixture__team__team_players=self.user.id
            ).count()

    def get_all_pairings(self):
        '''Method to return queryset of participating teams'''
        return Team.objects.filter(team_players=self.user)

    def get_game_win_percent(self):
        '''Method to return win percentage of games'''
        if self.get_all_games_played() > 0:
            return self.get_all_games_won() / self.get_all_games_played() * 100
        else:
            return 0

    def get_all_games_won(self):
        '''Method to return number of games won'''
        return Game.objects.filter(
            game_fixture__team__team_players=self.user.id,
            game_fixture__is_winner=True
            ).count()

    def get_all_games_lost(self):
        '''Method to return number of games lost'''
        return Game.objects.filter(
            game_fixture__team__team_players=self.user.id,
            game_fixture__is_winner=False
            ).count()

    def get_all_session_wins(self):
        '''Method to return number of session wins'''
        return Roster.objects.filter(
            player=self.user.id,
            is_winner=True
            ).count()

    def get_session_wins(self, group):
        '''Method to return number of session wins in a given group'''
        return Roster.objects.filter(
            player=self.user.id,
            session__group=group.id,
            is_winner=True
            ).count()

    def get_group_game_wins(self, group):
        '''Method to return number of game wins in a given group'''
        return Game.objects.filter(
            game_fixture__team__team_players=self.user.id,
            session__group=group,
            game_fixture__is_winner=True
            ).count()


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
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default='pending'
        )
    inbound = models.BooleanField(default=False)
    sent_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Friend Request model string representation"""
        if self.inbound is True:
            return f'{self.receiver} requested to join {self.session}'
        return f'{self.receiver} invited to {self.session}'

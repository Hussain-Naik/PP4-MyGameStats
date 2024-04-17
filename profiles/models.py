from django.db import models
from django.contrib.auth.models import User
from events.models import Session

# Create your models here.
class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    first_name = models.CharField(max_length=25,blank=True,null=True)
    last_name = models.CharField(max_length=25,blank=True,null=True)
    friends = models.ManyToManyField('self' ,blank=True,related_name='friends')

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
        if not profile in self.friends.all():
            self.friends.remove(profile)

    def unfriend(self, removee):
        self.remove_friend(removee)

        removee_profile = Profile.objects.get(user=removee)
        removee_profile.remove_friend(self)

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
        User,
        on_delete=models.CASCADE,
        related_name='session_invite_receiver'
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
    sent_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Friend Request model string representation"""
        return f'{self.receiver} invited to {self.session}'
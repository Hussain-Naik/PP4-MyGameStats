from django.db import models
from profiles.models import Profile

# Create your models here.
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
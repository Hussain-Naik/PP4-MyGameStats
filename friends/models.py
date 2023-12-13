from django.db import models
from profiles.models import Profile

# Create your models here.
class FriendRequest(models.Model):
    """Friend Request model"""
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

    sent_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    accepted = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)

    def __str__(self):
        """Friend Request model string representation"""
        return f'{self.sender} to {self.receiver}'
'''Signals for profile app'''
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from profiles.models import Profile, FriendRequest, SessionInvite


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Signal to create profile for a user"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=FriendRequest)
def post_save_add_friend(sender, created, instance, **kwargs):
    '''Signal add freind to both users and delete friend request'''
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.add_friend(receiver_)
        receiver_.add_friend(sender_)
        sender_.save()
        receiver_.save()
        instance.delete()


@receiver(post_save, sender=SessionInvite)
def post_save_accept_session_invite(sender, created, instance, **kwargs):
    '''Signal to add player to session and delete invite'''
    session_ = instance.session
    receiver_ = instance.receiver.user
    if instance.status == 'accepted':
        session_.add_player(receiver_)
        instance.delete()

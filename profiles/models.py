from django.db import models
from django.contrib.auth.models import User

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

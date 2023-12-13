from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    first_name = models.CharField(max_length=25,blank=True,null=True)
    last_name = models.CharField(max_length=25,blank=True,null=True)
    friends = models.ManyToManyField(User ,blank=True,related_name='friends')

    def __str__(self):
        """Profile model string representation"""
        return self.user.username

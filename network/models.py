from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission


class User(AbstractUser):
    
    groups = models.ManyToManyField(Group, related_name='network_users')
    user_permissions = models.ManyToManyField(Permission, related_name='network_user_permissions')
    
    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    text =  models.CharField(blank=False, null=False, max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True,)
    likes = models.IntegerField(default = '0')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f" {self.owner} : {self.text} "

class Network(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers" )
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following" )

    def __str__(self):
        return f" {self.follower} is following {self.following} "
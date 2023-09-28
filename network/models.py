from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    
    
    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()

class Post(models.Model):
    text =  models.CharField(blank=False, null=False, max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True,)


    def __str__(self):
        return f" {self.owner} "

class Network(models.Model):
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers" )
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following" )
    



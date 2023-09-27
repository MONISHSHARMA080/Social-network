from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    text =  models.CharField(blank=False, null=False, max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True,)

#returns what user started their tweet/text with(first word of it)
    def __str__(self):
        return f" {self.owner} "
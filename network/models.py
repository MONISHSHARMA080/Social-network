from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    text =  models.CharField(blank=False, null=False, max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        m =self.text.split(" ")
        return f" {self.owner} started with-> {m[0]}"
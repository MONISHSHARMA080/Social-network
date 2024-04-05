from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission

class User_in_magical_website(AbstractUser):
    profile_picture_url = models.URLField(null=True, blank=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    email_verified = models.BooleanField(null=False, blank=False, default=False)
    password = models.CharField(max_length=255, blank=True, null=True)
    verified_through_auth_provider = models.BooleanField(null=False, blank=False, default=False)
    # fro
    groups = models.ManyToManyField(Group, related_name='magical_website_users')
    user_permissions = models.ManyToManyField(Permission, related_name='magical_website_user_permissions')
    # 
    
    # def save(self, *args, **kwargs):
    #     # Check if the user is verified through the auth provider
    #     if self.verified_through_auth_provider:
    #         self.password = None  # Set password to NULL if verified
    #         self.email_verified = True
    #     else:
    #         self
        
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.username}"
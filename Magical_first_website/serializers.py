from rest_framework import serializers
from Magical_first_website.models import User_in_magical_website 

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_in_magical_website
        fields = ['name','email','email_verified','verified_through_auth_provider','password','profile_picture_url']
   
    # def create(self, validated_data):
    #     print(">>>>>>",super().create(validated_data))
    #     return super().create(validated_data)
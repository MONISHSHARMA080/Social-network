from rest_framework import serializers
from Magical_first_website.models import User_in_magical_website 

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_in_magical_website
        fields = []
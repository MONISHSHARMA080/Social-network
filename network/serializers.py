from rest_framework import serializers
from .models import User,Post,Network


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'owner' , 'date', 'likes' ]


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['following', 'followers']

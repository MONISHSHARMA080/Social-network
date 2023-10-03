from rest_framework import serializers
from .models import User,Post,Network


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['', '']

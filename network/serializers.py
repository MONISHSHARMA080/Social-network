from rest_framework import serializers
from .models import User,Post,Network

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'owner' , 'date', 'likes' , 'id'  ]

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['following', 'follower' , 'id']

#class UserSerializer(serializers.ModelSerializer):
    """ i think that this relation(primary key) will give all the posts and network associated woth the user  """
#    network = serializers.PrimaryKeyRelatedField(many=True, queryset=Network.objects.all())
#    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
#    class Meta:
#        model = User
#        fields = ['id', 'username', 'network' ]


# i thin the comment down was a mistake as i don't thin i need to filter the post based on user 
# as i can already do that with the primary key associated with it -->> although for all user I wanted for a 
# specific user for that i can in User_api view " User.objects.all() "  User.objects.filter(pk=id)
# for that -->> https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-url

#----------------###########------------------
  #   posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.filter(pk=id))
  #   see how to go about getting api for getting the post of a individual
#----------------###########------------------




class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
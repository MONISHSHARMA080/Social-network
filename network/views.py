from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from .models import User,Post,Network
from django.shortcuts import get_object_or_404

#----- rest framework--------

from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer , NetworkSerializer , UserSerializer , UserRegistrationSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
# for catching
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

#---simple JWT----

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

######################----------##################

""" API FOR  UPDATING DELEATING AND UPDATING PROFILE IS NOT BEING MADE AS WE DON'T NEED THAT  """

######################----------##################

#--------Djnago jwt(simple)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
#--------Djnago jwt(simple)



class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'statue' : 403, 'errors':serializer.errors, 'message':'something went wrong' })
        
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        refresh['username'] = user.username

        return Response({'statue' : 200,  'refresh':str(refresh), 'access':str(refresh.access_token) })










    # queryset = User.objects.all()
    # serializer_class = UserRegistrationSerializer


    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = self.perform_create(serializer)

    #     # Generating JWT token for the newly created user
    #     tokens = get_tokens_for_user(user)

    #     return Response(tokens, status=201)

    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     user.set_password(serializer.validated_data['password'])
    #     user.save()
    #     return user



# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             refresh_token = serializer.save()
#             print(MyTokenObtainPairView(refresh_token))
#             access_token = refresh_token.access_token
#             data = {
#                 "token_type": "access",
#                 "exp": access_token['exp'],
#                 "iat": access_token['iat'],
#                 "jti": access_token['jti'],
#                 "user_id": access_token['user_id'],
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndividualPost_api(generics.ListAPIView):
    """ will return a specific post based on id , where id is taken from url the  following users """
    serializer_class = PostSerializer
    
    def get_queryset(self):
       id = self.kwargs['pk']
       post = get_object_or_404(Post, pk=id)
       return [post] # making post iterable  


@permission_classes([IsAuthenticated])
class Follow_api(generics.ListAPIView):
    """ will return the post of all the  following users """
    serializer_class = PostSerializer
    
    def get_queryset(self):
#        user = self.request.user
        pk = self.kwargs['pk'] 
        user = User.objects.get(pk=pk)
        following_users = Network.objects.filter(follower=user).values_list('following', flat=True)
        posts = Post.objects.filter(owner__in=following_users).order_by('-date')
        return posts

class User_api(generics.RetrieveAPIView):
    """ will return all the post from a specific user  and who is following the user  """

    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs['pk'] 
        return User.objects.filter(pk=pk)


    def retrieve(self, request, *args, **kwargs):
# This line retrieves the User object based on the provided user ID from the URL.-->>https://www.django-rest-framework.org/api-guide/generic-views/#get_objectself
# however alt ways are-> def get(self, request, *args, **kwargs):
#        my_param = request.query_params.get('my_param')   and in serilizers in charfield and this too ->
        # id = request.user.id
        # data['posts'] = PostSerializer(posts, many=True).data
# self.request.query_params.get('')
        user = self.get_object()
        
# now we will filter posts  based on the user found in prev. line and get a relation 
        posts = Post.objects.filter(owner=user).order_by("-date")
        network = Network.objects.filter(following=user )
        serializer = self.get_serializer(user)
# JSON representation of the user
        data = serializer.data
# This line adds a list of serialized posts associated with the user to the data dictionary under the key 'posts'.
        data['posts'] = PostSerializer(posts, many=True).data
        data['network'] = NetworkSerializer(network, many=True).data
        return Response(data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class CreatePost(generics.CreateAPIView):
    """
    API view for creating a new Post using POST request.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        # serializer.save(owner=User.objects.get(pk=2))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Post_api(generics.ListCreateAPIView):
    """
    API view designed for creating a new Post through (HTTP) POST method
    and getting all post data e.g., on the home page.
    """
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializer
    

    def get_permissions(self):
        if self.request.method == 'POST':
            # Require authentication for POST requests
            return [permissions.IsAuthenticated()]
        else:
            # Allow unauthenticated users to make GET requests
            return []

    def create(self, request, *args, **kwargs):
        # Override the create method to set the user as the author of the post
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Post_rud_api(generics.RetrieveUpdateDestroyAPIView):
    """API view designed for HTTP methods GET (single post), PUT, PATCH, DELETE (of course of a single post)"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.owner == request.user:
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.owner == request.user:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)



@permission_classes([IsAuthenticated])
class Network_api(generics.ListCreateAPIView):
    """ this allows to make user follow other user """
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    def create(self, request, *args, **kwargs):
        following_id = request.data.get('following')
        follower_id = request.data.get('follower')
        network = Network.objects.filter(follower=follower_id , following=following_id)
        print(self.request.user.id)

        # Check if the entry already exists        
        network = Network.objects.filter(follower=follower_id, following=following_id).first()

        if network is not None:
            # If the network relationship already exists, return an error
            return Response({"detail": "You are already following this user."}, status=status.HTTP_400_BAD_REQUEST)

        # If the network relationship does not exist, create a new one
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
class Network_rud_api(generics.RetrieveUpdateDestroyAPIView):
    """ this allows to make user follow other user """
    serializer_class = NetworkSerializer
    # queryset = Network.objects.all()

    def get_queryset(self):
#        user = self.request.user
        # reteriving the user
        pk = self.kwargs['pk'] 
        pk_user = self.kwargs['pk_user']
        follower = User.objects.get(pk=pk)
        following = User.objects.get(pk=pk_user)
        return Network.objects.filter(follower= follower , following=following)



####----------api views over-------------------######


@login_required(login_url="/login")
def new_post(request):
    if request.method == "POST":
        text = request.POST["text"]
        p = Post(owner=request.user , text=text)
        p.save()
        return HttpResponseRedirect(reverse("index"))
    #else
    return render(request, "network/new_post.html")


def profile(request,id):

    #profile gets the id of the post owner
    # and then we get the user object of the post owner 
    user = User.objects.get(pk=id)
    #don't need this as name is already provides in username
    #name = user.get_short_name()

    # all post made by user
    all_post = Post.objects.filter(owner=id)
    posts = all_post.order_by("-date")

#seeing if user is currently following this profile owner
    try:
        check = Network.objects.get(following=user, follower=request.user.id)
    except Network.DoesNotExist:
        check = None

    return render(request, "network/profile.html", {"user":user, "posts":posts, "check":check})

@login_required(login_url="/login")
def follow(request,id):
    """"this allows users to follow other user
         ; where  id is the user to follow and request if from user who made it(follower)   """
    # having backend auth as a user can't  follow themself->
    
    # this is the id of user to follow
    user_to_follow = id
    to_follow = User.objects.get(pk=id)
    
    # Checking  if a  connection already exists
    existing_network = Network.objects.filter(follower=request.user, following=user_to_follow)
    if existing_network.exists():
        # Handle the case where the user is already following the target user
        return HttpResponse("You are already following this user.")
    elif to_follow.id==request.user.id:
        return render(request, "network/can't_follow_yourself.html")
    
    #adding to db  -> id=>user to follow and request.user.id=>follower
    n = Network(following = to_follow , follower = request.user)
    n.save()
    print( existing_network)
    return HttpResponseRedirect(reverse(index))

@login_required(login_url="/login")
def unfollow(request, id):
  """"this allows users to unfollow other user  
         ; where  id is the user to unfollow and request if from user who made it(follower)   """

  to_unfollow = User.objects.get(pk=id)
  row_from_network = Network.objects.get(follower=request.user, following=to_unfollow)
  row_from_network.delete()
  return HttpResponseRedirect(reverse(index))

@login_required(login_url="/login")
def following(request):
#1.>need to know who user follows   2.>filter each post where owner are ()multiple  
    user = request.user
#value_list returns a (sngle)tuple(of how many objects inside the ()  ) . wereas value returns a dict,so for sake of itereation 
    following = Network.objects.filter(follower = user).values_list('following', flat=True)
#here __in is sqlite3's somethin inside (,,,,,,)
    posts = Post.objects.filter(owner__in=following).order_by("-date")
    return render(request, "network/index.html", {"posts":posts})

@login_required(login_url="/login")
def edit(request,id):
    """returns the post to edit if sent a get request and if te request is POST(will do put when doing JS) update 
       the post """
    #user want  to write edit for post change -> show them this
    if request.method == "GET":
         post = Post.objects.get(pk=id)         
         return render(request, "network/edit.html", {"post":post})
    #else user submitted the change for the post so edit it
    new_text = request.POST["edit"]
    post = Post.objects.get(pk=id)
    post.text = new_text
    post.save()
    return HttpResponseRedirect(reverse(index))







def index(request):
    """ this returns/renders all the post user is going to see   """
    posts = Post.objects.order_by("-date").all()
    return render(request, "network/index.html", {"posts":posts})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



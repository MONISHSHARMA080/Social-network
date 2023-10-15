from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from .models import User,Post,Network

#----- rest framework--------

from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer , NetworkSerializer , UserSerializer 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
 
class Follow_api(generics.ListAPIView):
    """ will return the post of users following """
    serializer_class = PostSerializer
    
    def get_queryset(self):
#        user = self.request.user
        user = User.objects.get(pk=2)
        following_users = Network.objects.filter(follower=user).values_list('following', flat=True)
        posts = Post.objects.filter(owner__in=following_users).order_by('-date')
        return posts

class User_api(generics.RetrieveAPIView):
    """ will return all the post from a specific user  and who is following the user  """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
# This line retrieves the User object based on the provided user ID from the URL.-->>https://www.django-rest-framework.org/api-guide/generic-views/#get_objectself
# however alt ways are-> def get(self, request, *args, **kwargs):
#        my_param = request.query_params.get('my_param')   and in serilizers in charfield and this too ->
# self.request.query_params.get('')
        user = self.get_object()
# now we will filter posts  based on the user found in prev. line and get a relation 
        posts = Post.objects.filter(owner=user).order_by("-date")
        network = Network.objects.filter(following=user)
        serializer = self.get_serializer(user)
# JSON representation of the user
        data = serializer.data
# This line adds a list of serialized posts associated with the user to the data dictionary under the key 'posts'.
        data['posts'] = PostSerializer(posts, many=True).data
        data['network'] = NetworkSerializer(network, many=True).data
        return Response(data, status=status.HTTP_200_OK)





class CreatePost(generics.CreateAPIView):
    """
    API view for creating a new Post using POST request.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#    permission_classes = [IsAuthenticated]

    #def perform_create(self, serializer):
        # Assign the owner of the post based on the currently logged-in user
      #  serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
#        serializer.save(owner=self.request.user)
        serializer.save(owner=User.objects.get(pk=2))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Post_api(generics.ListCreateAPIView):
    """ api view designed for making a new Post through (HTTP) post method 
        and getting all post data eg on the home page    """
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializer

class Post_rud_api(generics.RetrieveUpdateDestroyAPIView):
    """ api view designed for HTTP method GET(single post) ,PUT, PATCH, DELETE (of course of a sngle post) """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#path("api/profile/<int:id>", views.Profile_api().as_view(), name="profile_api"),

######################----------##################

""" API FOR  UPDATING DELEATING AND UPDATING PROFILE IS NOT BEING MADE AS WE DON'T NEED THAT  """

######################----------##################

# think need auth for nowing which user send the request (can do it in the index page)


class Network_api(generics.ListCreateAPIView):
    """ this allows to make user follow other user """
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer     


# something wrong here
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

    
    

#class User_api(generics.ListCreateAPIView):
    """
        This view should return a list of all relationship(Network) and all the post of the user
        by determining id(pk) from the URL.
    """
#    queryset = User.objects.all()  ,<<<--- old 
#    serializer_class = UserSerializer
#    queryset = User.objects.all()




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



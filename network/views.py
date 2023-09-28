from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from .models import User,Post,Network



from .models import User

@login_required(login_url="/login")
def new_post(request):
    pass 
    if request.method == "POST":
        text = request.POST["text"]
        p = Post(owner=request.user , text=text)
        p.save()
        return HttpResponseRedirect(reverse("index"))
    #else
    return render(request, "network/new_post.html", {"new_post":New_post()})


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
        check = Network.objects.get(following=user, followers=request.user)
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
    existing_network = Network.objects.filter(followers=request.user, following=user_to_follow)
    if existing_network.exists():
        # Handle the case where the user is already following the target user
        return HttpResponse("You are already following this user.")
    elif to_follow.id==request.user.id:
        return render(request, "network/can't_follow_yourself.html")
    
    #adding to db  -> id=>user to follow and request.user.id=>follower
    n = Network(following = to_follow , followers= request.user)
    n.save()
    print( existing_network)
    return HttpResponseRedirect(reverse(index))


def unfollow(request, id):
  """"this allows users to unfollow other user  
         ; where  id is the user to unfollow and request if from user who made it(follower)   """

  to_unfollow = User.objects.get(pk=id)
  row_from_network = Network.objects.get(followers=request.user, following=to_unfollow)
  row_from_network.delete()
  return HttpResponseRedirect(reverse(index))


def following(request):
#1.>need to know who user follows   2.>filter each post where owner are ()multiple  
    user = request.user
#value_list returns a (sngle)tuple(of how many objects inside the ()  ) . wereas value returns a dict,so for sake of itereation 
    following = Network.objects.filter(followers=user).values_list('following', flat=True)
#here __in is sqlite3's somethin inside (,,,,,,)
    posts = Post.objects.filter(owner__in=following).order_by("-date")
    return render(request, "network/index.html", {"posts":posts})



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



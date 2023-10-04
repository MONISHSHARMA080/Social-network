
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("new_post", views.new_post, name="new_post"),
    path("register", views.register, name="register"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("follow/<int:id>", views.follow, name="follow"),
    path("unfollow/<int:id>", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),
    path("edit/<int:id>", views.edit, name="edit"),
    #------api----------
    path("api/post", views.posts_api, name="posts"),
    path("api/new_post", views.new_post_api, name="new_posts"),
    path("api/profile/<int:id>", views.profile_api, name="profile_api"),
    path("api/edit/<int:id>", views.edit_api, name="edit_api"),
    path("api/network", views.network_api, name="network_api"),
]
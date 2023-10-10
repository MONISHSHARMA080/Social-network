from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

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
    path("api/post", views.Post_api.as_view(), name="likes_api"),
    path("api/post-change/<int:pk>", views.Post_rud_api.as_view(), name="likes_rud_api"),
    path("api/networks/<int:id>", views.Network_api.as_view(), name="network_api"),
    path("api/networks-change/<int:pk>", views.Network_rud_api.as_view(), name="network_rud_api"),
    path('api/user/<int:pk>/', views.User_api.as_view(), name='user-posts-api'),]

urlpatterns = format_suffix_patterns(urlpatterns)
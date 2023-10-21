from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


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
    path("api/post/create", views.CreatePost.as_view(), name="create_api"),
    path("api/post-change/<int:pk>", views.Post_rud_api.as_view(), name="likes_rud_api"),
    path("api/networks/", views.Network_api.as_view(), name="network_api"),
    path("api/networks-change/<int:pk>/<int:pk_user>", views.Network_rud_api.as_view(), name="network_rud_api"),
    path('api/user/<int:pk>/', views.User_api.as_view(), name='user-posts-api'),
    path("api/network/<int:pk>", views.Follow_api.as_view(), name="network"),
    path("api/individual_post/<int:pk>", views.IndividualPost_api.as_view() ),
          #---api--JWT--
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from .views import views
from .views import auth_view


urlpatterns = [
    path('signup/google', auth_view.User.as_view()  ),  
    path('signup/email', auth_view.user_signup_by_email.as_view() ),  
    path('signup/spotify', auth_view.spotify_user_details ),  
    path('llm', views.response_from_llm, name='response_from_llm'),  
    path('verify', views.verify_google_token, name='verify_google_token'),  
]

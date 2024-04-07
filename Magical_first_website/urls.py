from django.urls import path
from .views import views
from .views import auth_view


urlpatterns = [
    path('signup/google', auth_view.User.as_view()  ),  
    path('users', auth_view.get_all_users  ),  
    path('llm', views.response_from_llm, name='response_from_llm'),  
    path('verify', views.verify_google_token, name='verify_google_token'),  
]

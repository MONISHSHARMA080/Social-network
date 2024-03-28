from django.urls import path
from . import views

urlpatterns = [
    path('', views.talk_to_llm, name='default'),  
    path('llm', views.response_from_llm, name='response_from_llm'),  
]

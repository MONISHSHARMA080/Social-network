from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Magical_first_website.models import User_in_magical_website
from Magical_first_website.serializers import user_serializer
from rest_framework import mixins
from rest_framework import generics

class User(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = User_in_magical_website.objects.all()
    serializer_class = user_serializer
    
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)
from django.http import JsonResponse
from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Magical_first_website.models import User_in_magical_website
from Magical_first_website.serializers import Email_signup_usewr_serializer, Spotify_signup_user_serializer, View_all_users_serializer, user_serializer
from rest_framework import mixins
from rest_framework import generics
from .views import verify_google_token
from rest_framework import status
from rest_framework.decorators import api_view


class User(generics.GenericAPIView, mixins.ListModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin,):
    queryset = User_in_magical_website.objects.all()
    serializer_class = user_serializer
    
    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data )
        if not serializer.is_valid():
            return Response( serializer.data ,status=status.HTTP_400_BAD_REQUEST)
            
        a = serializer.save()
        print(a,"----")
        
        return Response(a)
    
    def get(self, request, *args, **kwargs):
        users = User_in_magical_website.objects.all()
        serializer = View_all_users_serializer(users, many=True)
        return Response(serializer.data)

    
    def delete(self, request, *args, **kwargs):
        users = self.get_queryset()
        users.delete()
        return Response( status=204)
    
    
class user_signup_by_email(mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = User_in_magical_website.objects.all()
    serializer_class = Email_signup_usewr_serializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data )
        if not serializer.is_valid():
            return Response( serializer.data ,status=status.HTTP_400_BAD_REQUEST)
            
        a = serializer.save()
        print(a,"----")
        
        return Response(a)    
    
 
    
class user_signup_by_spotify(mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = User_in_magical_website.objects.all()
    serializer_class = Spotify_signup_user_serializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data )
        if not serializer.is_valid():
            return Response( serializer.data ,status=status.HTTP_400_BAD_REQUEST) 
        response_from_create_func_in_serilizer  = serializer.save()
        print(response_from_create_func_in_serilizer,"----from spotify serilizer")
        
        return Response(response_from_create_func_in_serilizer)    

    
    
    
# ---helper function remove as we moved it to serilizers.py---
     
def verify_google_token_view(request_object):
        id_token_from_frontend = request_object.data.get('id_token')
        
        if not id_token_from_frontend:
            return { "message": "Bad request: id_token is missing", "status" : 400}

        # Calling the verify_google_token function
        id_info = verify_google_token(id_token_from_frontend)
        
        return  id_info

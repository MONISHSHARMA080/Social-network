from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Magical_first_website.models import User_in_magical_website
from Magical_first_website.serializers import user_serializer
from rest_framework import mixins
from rest_framework import generics
from .views import verify_google_token


class User(generics.GenericAPIView):
    queryset = User_in_magical_website.objects.all()
    serializer_class = user_serializer
    
    def post(self, request, *args, **kwargs):
        print("----++----")
        response_from_token_verification = verify_google_token_view(request)
        print(response_from_token_verification)
        print("----++----")
        
        serializer = self.get_serializer(data={
            "profile_picture_url":response_from_token_verification.get('picture'), "email_verified":response_from_token_verification.get('email_verified'),
            
        })
        print(serializer.is_valid(), "pPPpPppppPppPpPppP")
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        return Response(response_from_token_verification, status=response_from_token_verification['status'])
    
  
def verify_google_token_view(request_object):
    id_token_from_frontend = request_object.data.get('id_token')
    

    if not id_token_from_frontend:
        return { "message": "Bad request: id_token is missing", "status" : 400}

    # Calling the verify_google_token function
    id_info = verify_google_token(id_token_from_frontend)
    
    return  id_info
    
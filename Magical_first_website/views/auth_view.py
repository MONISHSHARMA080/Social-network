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


class User(generics.GenericAPIView, mixins.ListModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin,):
    queryset = User_in_magical_website.objects.all()
    serializer_class = user_serializer
    
    def post(self, request, *args, **kwargs):
        
        
        response_from_token_verification = verify_google_token_view(request)

        # print("----++----")
        # print(response_from_token_verification )
        # print("----++----")
        
        # serializer = self.get_serializer(data={
        #     "profile_picture_url":response_from_token_verification.get('picture'),
        #     "email_verified":e,
        #     "verified_through_auth_provider": e,
        #     "email":response_from_token_verification.get('email'),
        #     "name":response_from_token_verification.get('given_name'),
        # })
        print("---in post ")
        serializer = self.get_serializer(data=request.data )
        a = serializer.is_valid()
        print("serilizer is valid ",a)
        serializer.save()
    
        # return Response(response_from_token_verification, status=response_from_token_verification['status'])
        return Response({"response_from_token_verification, status=response_from_token_verification['status']":"KHIB"})
    
    def perform_create(self, serializer):
        print("---in perform create ")
        serializer.save()
    
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        users = self.get_queryset()
        users.delete()
        return Response( status=204)
        
    
  
def verify_google_token_view(request_object):
    id_token_from_frontend = request_object.data.get('id_token')
    

    if not id_token_from_frontend:
        return { "message": "Bad request: id_token is missing", "status" : 400}

    # Calling the verify_google_token function
    id_info = verify_google_token(id_token_from_frontend)
    
    return  id_info
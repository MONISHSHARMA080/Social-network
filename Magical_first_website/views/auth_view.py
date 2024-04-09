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
    
    
@api_view(['GET'])
def spotify_user_details(request):
    
    access_token = 'AQDS4Xp_gueWBmqbtQRMRE8Oy0EiPZ7jVXQx2CdtZYaqKPdmYJQllIy5H2948opx0haIRP-LZwVv6NlboRPGT3eqZEWF-ja8DXTyzib9EvY_Nf92cNrbqysu5Vr-G_-ytq8GUtuhh4vU6rt7JZuA5pEfBArXbjZcyKl9z2_9gKltRgWLdktvzUP-UBQVkl4BmDqx'
    # Define the parameters required for exchanging authorization code for access token
    code = access_token  # Authorization code obtained from React Native app
    
    redirect_uri = 'magicalfirstwebsite://redirect'
    grant_type = 'authorization_code'
    client_id =  '812c827d57b44b2497941ccb210ae022'
    client_secret = 'd2dabccf5df64a78bd88454de770ebc0'
    authorization_without_encoding = F"{client_id}:{client_secret}"
    authorization = base64.b64encode(authorization_without_encoding.encode()).decode()
    url = 'https://accounts.spotify.com/api/token'
    data = {
        "form":{"grant_type":grant_type,"code":code,"redirect_uri":redirect_uri},
        "header":{"Authorization":f"Basic {authorization}"}
    }
    response = requests.post(url,data=data["form"],headers=data["header"])
    print("-------------------------")
    print(f"------{response.status_code}-------------------")
    print(response.json(), "response __--__-_-_--  _--_-____")
    print("-------------------------")
    print("-------------------------")
    if response.status_code == 200:
        # now after getting access token from user's token , getting user details 
        access_token_for_getting_user_details_from_api = response.json().get('access_token')
        print(access_token_for_getting_user_details_from_api)
        url_to_get_user_details_from_spotify = 'https://api.spotify.com/v1/me'
        response_containing_user_details = requests.get(url=url_to_get_user_details_from_spotify, headers={"Authorization": f"Bearer {access_token_for_getting_user_details_from_api}"})
        print("[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]")
        if response_containing_user_details.status_code == 200:
            print(response_containing_user_details.json())
            return Response(status=response.status_code,data=response_containing_user_details)
        print(response_containing_user_details.status_code,response_containing_user_details.content)
        print("[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]")
        
    return Response(status=response.status_code,data=response)
    
    
class user_signup_by_spotify(mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = User_in_magical_website.objects.all()
    serializer_class = Spotify_signup_user_serializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data )
        if not serializer.is_valid():
            return Response( serializer.data ,status=status.HTTP_400_BAD_REQUEST) 
        a = serializer.save()
        print(a,"----from spotify serilizer")
        
        return Response(a)    

    
    
    
# ---helper function remove as we moved it to serilizers.py---
     
def verify_google_token_view(request_object):
        id_token_from_frontend = request_object.data.get('id_token')
        
        if not id_token_from_frontend:
            return { "message": "Bad request: id_token is missing", "status" : 400}

        # Calling the verify_google_token function
        id_info = verify_google_token(id_token_from_frontend)
        
        return  id_info

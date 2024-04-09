from rest_framework import serializers
from Magical_first_website.models import User_in_magical_website 
from Magical_first_website.views.views import verify_google_token 
# password hashing --
from django.contrib.auth.hashers import make_password
import requests
import base64

class user_serializer(serializers.ModelSerializer):
    id_token = serializers.CharField(write_only=True,max_length=None, min_length=10, allow_blank=False, trim_whitespace=True) 

    class Meta:
        model = User_in_magical_website
        fields = ['id_token']

    def create(self, validated_data):
        id_token = validated_data.pop('id_token') 
        response_from_google_auth_function = verify_google_token_view(id_token)
         
        if response_from_google_auth_function.get('status') == 400:
            print(response_from_google_auth_function.get('status'))
            # if the response from the google system is a bad request we will warn user that your token is invalid and message from google auth
            return {"status":400, "message":response_from_google_auth_function.get('exception') }
        #else if status is 200 
        elif response_from_google_auth_function.get('status') == 200:
            # fitting it in the model
            validated_data['name'] = response_from_google_auth_function.get('given_name')
            if validated_data['name'] =="": # why -> i am not sure if one of them m is empty or not  so just  to be safe    
                validated_data['name'] = response_from_google_auth_function.get('name') 
            validated_data['email'] = response_from_google_auth_function.get('email')
            validated_data['profile_picture_url'] = response_from_google_auth_function.get('picture', '')
            validated_data['email_verified'] = response_from_google_auth_function.get('email_verified', '')  
            validated_data['verified_through_auth_provider'] = response_from_google_auth_function.get('email_verified', '')
        
        
        
        super().create(validated_data)
        return {"status":response_from_google_auth_function.get('status'),"message":validated_data}
   
class View_all_users_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_in_magical_website
        # fields = '__all__'
        exclude = ['groups','user_permissions']
        
class Email_signup_usewr_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_in_magical_website
        # fields = '__all__'
        exclude = ['groups','user_permissions' , 'verified_through_auth_provider','email_verified','registered_date']
        
    def create(self, validated_data):
        # when if we have validated data just take it and just  hash the password(add salt)  before storing it
        validated_data['password'] =  make_password(validated_data.get('password'))
        # setting the email verified to be false by default here --not as it is set by defalut
        super().create(validated_data)
        return {"status":"response_from_google_auth_function.get('status')","message":validated_data}
        
class Spotify_signup_user_serializer(serializers.ModelSerializer):
    id_token = serializers.CharField(write_only=True,max_length=None, min_length=10, allow_blank=False, trim_whitespace=True) 
    
    class Meta:
        model = User_in_magical_website
        fields = ['id_token']
        # exclude = ['groups','user_permissions' , 'verified_through_auth_provider','email_verified','registered_date']
        
    def create(self, validated_data):
        # when if we have validated data just take it and just  hash the password(add salt)  before storing it
        code = validated_data.pop('id_token')
        
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
            # now after getting access token from user's token , getting user details from the access token  
            access_token_for_getting_user_details_from_api = response.json().get('access_token')
            print(access_token_for_getting_user_details_from_api)
            url_to_get_user_details_from_spotify = 'https://api.spotify.com/v1/me'
            response_containing_user_details = requests.get(url=url_to_get_user_details_from_spotify, headers={"Authorization": f"Bearer {access_token_for_getting_user_details_from_api}"})
            print("[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]")
            if response_containing_user_details.status_code == 200:
                print(response_containing_user_details.json(),"KKKKKKKKKKKKKKKKKKKKKKKKKK")
                response_containing_user_details = response_containing_user_details.json()
                validated_data['name'] = response_containing_user_details.get('display_name')
                validated_data['email'] = response_containing_user_details.get('email')
                images = response_containing_user_details.get('images')
                if images:
                    validated_data['profile_picture_url'] = images[0].get('url')
                validated_data['email_verified'] = 'True' # as we are using spotify's api
                validated_data['verified_through_auth_provider'] = 'True'
                print(validated_data , "??//?//?")
                super().create(validated_data)
                return {"status":response.status_code,"data":response_containing_user_details,"message":validated_data ,"k":"ppPpPPppppppPp"}
            print(response_containing_user_details.status_code,response_containing_user_details.content)
            print("[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]----") 
        
        return {"status":"response_from_google_auth_function.get('status')","message":validated_data}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# auth helper function----------------
def verify_google_token_view(request_object):
        print("verifying id tokken from serilizers ---+00----")
        id_token_from_frontend = request_object
        

        if not id_token_from_frontend:
            return { "message": "Bad request: id_token is missing", "status" : 400}

        # Calling the verify_google_token function
        response_from_google_auth_function = verify_google_token(id_token_from_frontend)
        
        return  response_from_google_auth_function


def verify_spotify_token_view(request_object):
        print("verifying id tokken from serilizers ---+00----")
        id_token_from_frontend = request_object
        

        if not id_token_from_frontend:
            return { "message": "Bad request: id_token is missing", "status" : 400}

        # Calling the verify_google_token function
        response_from_google_auth_function = verify_spotify_token(id_token_from_frontend)
        
        return  response_from_google_auth_function


from rest_framework import serializers
from Magical_first_website.models import User_in_magical_website 
from Magical_first_website.views.views import verify_google_token 
# password hashing --
from django.contrib.auth.hashers import make_password

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
    class Meta:
        model = User_in_magical_website
        # fields = '__all__'
        # exclude = ['groups','user_permissions' , 'verified_through_auth_provider','email_verified','registered_date']
        
    def create(self, validated_data):
        # when if we have validated data just take it and just  hash the password(add salt)  before storing it
        validated_data['password'] =  make_password(validated_data.get('password'))
        # setting the email verified to be false by default here --not as it is set by defalut
        super().create(validated_data)
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


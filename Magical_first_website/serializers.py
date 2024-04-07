from rest_framework import serializers
from Magical_first_website.models import User_in_magical_website 
# from .views.auth_view import verify_google_token_view
# from Magical_first_website.views.auth_view import verify_google_token_view
from Magical_first_website.views.views import verify_google_token 

class user_serializer(serializers.ModelSerializer):
    id_token = serializers.CharField(write_only=True,max_length=None, min_length=10, allow_blank=False, trim_whitespace=True) 

    class Meta:
        model = User_in_magical_website
        fields = ['id_token']

    def create(self, validated_data):
        print("----form serilizer---")
        print(")000))0",validated_data)
        id_token = validated_data.pop('id_token') 
        print(")000))0", id_token)
        id_info = verify_google_token_view(id_token)
        print(id_info,"<--K_k_,-_,,_,_<,_<-,-,")
         
        if id_info.get('status') == 400:
            print(id_info.get('status'))
            # if the response from the google system is a bad request we will warn user that your token is invalid and message from google auth
            return {"status":400, "message":id_info.get('exception') }
        #else if status is 200 
        elif id_info.get('status') == 200:
            # fitting it in the model
            validated_data['name'] = id_info.get('given_name')
            if validated_data['name'] =="": # why -> i am not sure if one of them m is empty or not  so just  to be safe    
                validated_data['name'] = id_info.get('name') 
            validated_data['email'] = id_info.get('email')
            validated_data['profile_picture_url'] = id_info.get('picture', '')
            validated_data['email_verified'] = id_info.get('email_verified', '')  
            validated_data['verified_through_auth_provider'] = id_info.get('email_verified', '')
        
        
        
        super().create(validated_data)
        return {"status":id_info.get('status'),"message":validated_data}
    
def verify_google_token_view(request_object):
        print("verifying id tokken from serilizers ---+00----")
        id_token_from_frontend = request_object
        

        if not id_token_from_frontend:
            return { "message": "Bad request: id_token is missing", "status" : 400}

        # Calling the verify_google_token function
        id_info = verify_google_token(id_token_from_frontend)
        
        return  id_info
   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_in_magical_website
        fields = '__all__'
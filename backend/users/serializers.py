from rest_framework import serializers
from pydantic import ValidationError
from core.schemas import *# <-- Import the Pydantic models
import core.db_utils as db_utils
from django.contrib.auth.hashers import make_password # <-- Import Django's hashing function

class PydanticUserRegistrationSerializer(serializers.Serializer):
    """
    This DRF Serializer acts as a bridge to our Pydantic model.
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, 
                                     required=True,
                                     style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, 
                                     required=True,
                                     style={'input_type': 'password'})
    
    def validate(self, attrs):
        """
        This is the validation hook where we hand off to Pydantic.
        DRF calls this method with the incoming request data.
        """
        try:
            UserRegisterSchema(**attrs)
            return attrs
        except ValidationError as e:
            raise serializers.ValidationError(e.errors())
        
    def create(self, validated_data):
        # Safely get the plain-text password from the SecretStr object
        password = validated_data.get('password').get_secret_value()
        
        # FIX 3: Construct the full user document to be saved.
        # This ensures the data saved to your DB is consistent with your schema.
        user_document_to_save = {
            "email": validated_data.get('email'),
            "display_name": validated_data.get('email').split('@')[0], # A sensible default
            "password_hash": make_password(password),
            "sources": [], # Initialize with empty lists
            "liked_posts": [],
        }

        new_user = db_utils.create_user(user_document_to_save)
        new_user.pop('password_hash', None)
        return new_user


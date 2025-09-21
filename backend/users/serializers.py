from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        #min_length=6, 
        #validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'password_confirm',
            'display_name'
        ]
    
    def validate(self, attrs):
        print("=== VALIDATE METHOD CALLED ===")
        print(f"Received attrs: {attrs}")
        
        if attrs['password'] != attrs['password_confirm']:
            print("Password mismatch error")
            raise serializers.ValidationError("Passwords don't match")
        
        print("Validation passed")
        return attrs
    
    def create(self, validated_data):
        print("=== CREATE METHOD CALLED ===")
        print(f"Validated data: {validated_data}")
        
        validated_data.pop('password_confirm')
        print(f"After removing password_confirm: {validated_data}")
        
        try:
            user = User.objects.create_user(
                username=validated_data['email'],
                email=validated_data['email'],
                password=validated_data['password'],
                display_name=validated_data.get('display_name', ''),
            )
            print(f"User created successfully: {user.email}")
            return user
        except Exception as e:
            print(f"Error creating user: {e}")
            raise
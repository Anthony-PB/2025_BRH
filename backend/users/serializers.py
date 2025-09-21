from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.apps import apps
from django.contrib.auth.password_validation import validate_password
from aggregator.models import Source
User = get_user_model()


from rest_framework import serializers
from django.contrib.auth import get_user_model
from aggregator.models import Source

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, 
    #validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'display_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            display_name=validated_data.get('display_name', ''),
        )
        return user

class UserFollowSerializer(serializers.ModelSerializer):
    followed_sources = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'display_name', 'followed_sources']
        read_only_fields = ['id', 'email']

    def get_followed_sources(self, obj):
        # Return full source info for each ID the user follows
        return list(Source.objects.filter(id__in=obj.followed_source_ids).values(
            'id', 'name', 'base_url', 'feed_url', 'category', 'is_rss'
        ))
    
class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=6,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]
    
    def validate(self, attrs):
        
        if not User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError("Email is not registered to a user.")

        user = User.objects.get(email=attrs['email'])
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("The password is incorrect.")

        return attrs
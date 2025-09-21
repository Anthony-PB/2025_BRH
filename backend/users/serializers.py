from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from aggregator.models import Source
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=6,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
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
        
        validated_data.pop('password_confirm')
        
        try:
            user = User.objects.create_user(
                username=validated_data['email'],
                email=validated_data['email'],
                password=validated_data['password'],
                display_name=validated_data.get('display_name', ''),
            )
            return user
        except Exception as e:
            raise

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
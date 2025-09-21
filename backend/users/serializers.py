from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.apps import apps
from django.contrib.auth.password_validation import validate_password
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
            'password_confirm',
            'first_name',
            'last_name',
            'display_name'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        # Remove password_confirm as it's not needed for user creation
        validated_data.pop('password_confirm')

        # Create user with Django's built-in method
        user = User.objects.create_user(
            username=validated_data['email'],  # Use email as username
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
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
        # Lazy import to avoid circular imports
        Source = apps.get_model('aggregator', 'Source')
        return list(Source.objects.filter(id__in=obj.followed_source_ids).values(
            'id', 'name', 'base_url', 'feed_url', 'category', 'is_rss'
        ))

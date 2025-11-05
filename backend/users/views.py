from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from aggregator.models import Source

User = get_user_model()


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        
        # Use UserSerializer to include followed_sources
        user_data = UserSerializer(user).data

        return Response({
            'message': 'User created successfully',
            'user': user_data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer # Use the new general-purpose serializer

    def get_object(self):
        """
        Override this method to ensure users can only
        view, update, or delete their own profile.
        """
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )


class FollowSourceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, source_id):
        user = request.user
        try:
            source = Source.objects.get(id=source_id)
        except Source.DoesNotExist:
            return Response({'error': 'Source not found'}, status=status.HTTP_404_NOT_FOUND)

        user.followed_sources.add(source)
        user_data = UserSerializer(user).data
        return Response(user_data, status=status.HTTP_200_OK)

    def delete(self, request, source_id):
        user = request.user
        try:
            source = Source.objects.get(id=source_id)
        except Source.DoesNotExist:
            return Response({'error': 'Source not found'}, status=status.HTTP_404_NOT_FOUND)

        user.followed_sources.remove(source)
        user_data = UserSerializer(user).data
        return Response(user_data, status=status.HTTP_200_OK)


class LoginUserView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        # Use UserSerializer to include followed_sources
        user_data = UserSerializer(user).data

        return Response({
            'message': 'Login successful',
            'user': user_data,
            'token': token.key
        }, status=status.HTTP_200_OK)
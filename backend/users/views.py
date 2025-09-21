from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserFollowSerializer, UserLoginSerializer
# Make sure this import path matches your project structure
from aggregator.models import Source
from django.contrib.auth import authenticate

User = get_user_model()



class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            # Create authentication token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'message': 'User created successfully',
                'user': {
                    'id': str(user.id),
                    'email': user.email,
                    'display_name': getattr(user, 'display_name', ''),
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                },
                'token': token.key  # Add this line
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegistrationSerializer
    
    def get_object(self):
        """
        Override this method to ensure users can only
        view, update, or delete their own profile.
        """
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        """
        Custom logic for when a user is deleted.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        # You can add custom logic here, like logging out the user
        # TODO: Think about logging out?
        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )

class FollowSourceView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, source_id):
        user = request.user
        if not Source.objects.filter(id=source_id).exists():
            return Response({'error': 'Source not found'}, status=status.HTTP_404_NOT_FOUND)

        user.follow_source(source_id)
        return Response({'message': 'Source followed successfully'}, status=status.HTTP_200_OK)


class UnfollowSourceView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, source_id):
        user = request.user
        if not Source.objects.filter(id=source_id).exists():
            return Response({'error': 'Source not found'}, status=status.HTTP_404_NOT_FOUND)

        user.unfollow_source(source_id)
        return Response({'message': 'Source unfollowed successfully'}, status=status.HTTP_200_OK)
    
class LoginUserView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({
                'error': 'Email and password required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Use Django's authenticate which handles password hashing
        user = authenticate(username=email, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'message': 'Login successful',  # Fixed message
                'user': {
                    'id': str(user.id),
                    'email': user.email,
                    'display_name': getattr(user, 'display_name', ''),
                },
                'token': token.key
            }, status=status.HTTP_200_OK)  # Fixed status code
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)